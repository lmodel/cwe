#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Check MITRE's CWE pages against the edition the schema renders.

The schema renders the CWE List and its XML Schema (XSD) at the versions pinned
below, and upstream/ holds those files unchanged. Four things can change without
any change in this repository:

- MITRE publishes another edition of the CWE List;
- the pinned XSD or the file behind the "latest" XSD link changes;
- MITRE lists another schema version on its archive page;
- the Terms of Use change.

The script reads MITRE's public pages and compares each file by git object hash.
It prints a Markdown report, and exits 1 when:

- the latest catalogue is another version or date, or holds other bytes;
- the versioned XSD changed or is gone;
- the file behind the "latest" XSD link changed, which includes MITRE fixing the
  known mismatch below, since the pin and the docs then move;
- the archive page lists a schema version newer than the pinned one;
- the Terms of Use changed;
- a check could not finish, such as a refused or failed request, or an answer
  larger than the script reads.

A newer version of the parallel 4.x line, which keeps schema 7.x for existing
consumers, is reported for information only, because this schema does not render it.

Text a server chose is quoted as code on one line in the report, so the issue the
workflow opens from it cannot mention anyone. A redirect is followed only to an https
address on cwe.mitre.org. The script sends no token. Usage::

    python scripts/check_upstream_release.py [--report FILE]
"""

from __future__ import annotations

import argparse
import hashlib
import html
import http.client
import io
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

USER_AGENT = "lmodel-cwe-watch"
SITE = "https://cwe.mitre.org"
# The one host a redirect may lead to.
HOSTS = frozenset({"cwe.mitre.org"})

# The most the script reads of one answer. The largest, the catalogue's ZIP, is
# about 2 MB, and the XML inside it about 19 MB.
MAX_BYTES = 20_000_000
MAX_XML_BYTES = 200_000_000

# The edition the schema renders, its date, its XSD and the XSD's canonical address.
# tests/test_upstream.py holds the schema headers and these pins equal. Move them
# together, with upstream/ and the headers, for another edition.
PINNED_EDITION = "5.0"
PINNED_DATE = "2026-10-28"
PINNED_XSD_VERSION = "8.0"
PINNED_SOURCE = f"{SITE}/data/xsd/cwe_schema_v8.0.xsd"
CATALOGUE_URL = f"{SITE}/data/xml/cwec_latest.xml.zip"
LATEST_XSD_URL = f"{SITE}/data/xsd/cwe_schema_latest.xsd"
ARCHIVE_URL = f"{SITE}/data/archive.html"
TERMS_URL = f"{SITE}/about/termsofuse.html"

# Each file upstream/ holds, with its git object hash. tests/test_upstream.py holds
# upstream/ to this list.
PINNED_BLOBS = {
    "README.md": "f987bbcf002d75806fa4e75e73f950aee9a7e3a3",
    "TERMS.txt": "077b38db3dafe40497fb1d2e71b3e1ed2db0749b",
    "cwe_schema_v8.0.xsd": "fd9a9778c3df5804d24fec960682561062a20ce2",
    "cwec_v5.0.xml.zip": "951bcc7e96e244937590231080c5717f38e1ff1c",
}
# The XML inside the catalogue's ZIP, by its git object hash. A ZIP can be packed
# again without any change to what it holds.
PINNED_XML_BLOB = "6533b3adc1f76079c5de4c0f5ebaf817e0812caf"

# The file behind the "latest" XSD link as it stood on 2026-11-04. It is not the
# versioned file: it is an earlier copy, last modified on 2026-10-27 at 19:46 UTC, 32
# minutes before the versioned one, and the catalogue breaks it in 69 places, while
# the catalogue validates against the versioned file with no error. See docs/about.md.
PINNED_LATEST_XSD_BLOB = "13c943498133d5eb7e0defd6931b0158e5009512"

# The newest schema version of each line on the archive page, read on 2026-11-04.
# Schema 7.x carries the parallel 4.x editions for existing consumers.
PINNED_PARALLEL_XSD_VERSION = "7.4"

TERMS_START = "CWE&trade; is free to use"
TERMS_END = "Page Last Updated"


class _ExpectedHostRedirect(urllib.request.HTTPRedirectHandler):
    """Follow a redirect only to an https address on one of HOSTS."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        parts = urllib.parse.urlsplit(newurl)
        if parts.scheme != "https" or parts.hostname not in HOSTS:
            raise ValueError(f"a redirect leads off the expected hosts, to {newurl}")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


# An opener in place of urlopen's, whose redirect handler follows any address.
_open = urllib.request.build_opener(_ExpectedHostRedirect).open


def _get(url: str) -> bytes:
    """The body of an answer from MITRE's site, read up to the cap."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with _open(req, timeout=60) as resp:
        body = resp.read(MAX_BYTES + 1)
    if len(body) > MAX_BYTES:
        raise ValueError(f"the answer from {url} is larger than {MAX_BYTES} bytes")
    return body


def _code(text: object) -> str:
    """Text a server chose, as a code span on one line, so it cannot mention a
    person or add a link in the issue. A blank line would end the span, so
    every run of spaces and line breaks is one space."""
    return "`" + " ".join(str(text).replace("`", "'").split()) + "`"


def blob(data: bytes) -> str:
    """The git object hash of a file's bytes."""
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def terms_text(page: bytes) -> str:
    """The Terms of Use from the page: a paragraph per line, no markup."""
    text = page.decode("utf-8", errors="replace")
    start, end = text.find(TERMS_START), text.find(TERMS_END)
    if start < 0 or end < start:
        raise ValueError("the Terms of Use page has another shape")
    body = re.sub(r"</(p|h\d)>", "\n", text[start:end])
    body = html.unescape(re.sub(r"<[^>]+>", " ", body))
    lines = [" ".join(line.split()) for line in body.splitlines()]
    return "\n\n".join(line for line in lines if line) + "\n"


def read_catalogue(archive: bytes) -> tuple[dict[str, str], bytes]:
    """The root element's attributes and the XML bytes of a catalogue's ZIP."""
    with zipfile.ZipFile(io.BytesIO(archive)) as opened:
        members = [i for i in opened.infolist() if i.filename.endswith(".xml")]
        if len(members) != 1:
            raise ValueError(f"the ZIP holds {len(members)} XML files, not one")
        if members[0].file_size > MAX_XML_BYTES:
            raise ValueError("the XML in the ZIP is larger than the script reads")
        data = opened.read(members[0])
    _, root = next(ET.iterparse(io.BytesIO(data), events=("start",)))
    return dict(root.attrib), data


def check_catalogue() -> tuple[list[str], bool]:
    """Report whether the latest catalogue is the pinned edition, byte for byte."""
    attributes, data = read_catalogue(_get(CATALOGUE_URL))
    version, date = attributes.get("Version"), attributes.get("Date")
    if version != PINNED_EDITION or date != PINNED_DATE:
        return [
            f"- **The latest CWE List is version {_code(version)} of {_code(date)}; "
            f"the schema renders {PINNED_EDITION} of {PINNED_DATE}.** Read what "
            "changed, decide whether the schema moves to it, and move upstream/, the "
            "pins here and the schema headers together."
        ], True
    if blob(data) != PINNED_XML_BLOB:
        return [
            f"- **The XML of CWE {PINNED_EDITION} changed under the same version.** "
            "Find out what changed before trusting the copy in upstream/."
        ], True
    return [f"- The latest CWE List is the pinned edition, {PINNED_EDITION}."], False


def check_schemas() -> tuple[list[str], bool]:
    """Report whether the versioned XSD and the "latest" link hold the pinned files."""
    report, attention = [], False
    versioned = blob(_get(PINNED_SOURCE))
    if versioned != PINNED_BLOBS["cwe_schema_v8.0.xsd"]:
        attention = True
        report.append(
            f"- **{PINNED_SOURCE} changed.** Read what changed, then move "
            "upstream/ and the pin, or find out why a published XSD moved."
        )
    else:
        report.append(f"- XSD {PINNED_XSD_VERSION} is the pinned file.")
    latest = blob(_get(LATEST_XSD_URL))
    if latest == versioned:
        attention = True
        report.append(
            f"- **{LATEST_XSD_URL} now holds the same file as XSD "
            f"{PINNED_XSD_VERSION}.** MITRE has fixed the mismatch: drop the pin "
            "and the sentence on it in docs/about.md."
        )
    elif latest != PINNED_LATEST_XSD_BLOB:
        attention = True
        report.append(
            f"- **{LATEST_XSD_URL} changed, and is not XSD {PINNED_XSD_VERSION}.** "
            "It may be a newer schema, or another copy of this one."
        )
    else:
        report.append(
            f"- The 'latest' XSD link still holds an earlier copy of XSD "
            f"{PINNED_XSD_VERSION}, as pinned."
        )
    return report, attention


def _version(text: str) -> tuple[int, ...]:
    return tuple(int(part) for part in text.split("."))


def check_lines() -> tuple[list[str], bool]:
    """Report any schema version the archive page lists beyond the pinned ones."""
    page = _get(ARCHIVE_URL).decode("utf-8", errors="replace")
    found = set(re.findall(r"cwe_schema_v(\d+(?:\.\d+)+)\.xsd", page))
    if PINNED_XSD_VERSION not in found:
        return [
            f"- **The archive page no longer lists XSD {PINNED_XSD_VERSION}.** Read "
            "the page and find out what happened."
        ], True
    newer = sorted(
        (v for v in found if _version(v) > _version(PINNED_XSD_VERSION)), key=_version
    )
    if newer:
        return [
            "- **The archive page lists a newer schema: "
            + ", ".join(_code(v) for v in newer)
            + ".** Read what changed and whether the schema moves to it."
        ], True
    parallel = sorted(
        (
            v
            for v in found
            if _version(PINNED_PARALLEL_XSD_VERSION)
            < _version(v)
            < _version(PINNED_XSD_VERSION)
        ),
        key=_version,
    )
    if parallel:
        return [
            "- For information, the parallel 4.x line has moved to schema "
            + ", ".join(_code(v) for v in parallel)
            + ". This schema does not render it."
        ], False
    return [
        f"- The archive page lists no schema beyond {PINNED_XSD_VERSION} and "
        f"{PINNED_PARALLEL_XSD_VERSION}."
    ], False


def check_terms() -> tuple[list[str], bool]:
    """Report whether the Terms of Use are the pinned text."""
    text = terms_text(_get(TERMS_URL))
    if blob(text.encode("utf-8")) != PINNED_BLOBS["TERMS.txt"]:
        return [
            f"- **The Terms of Use changed at {TERMS_URL}.** Read what changed, "
            "update NOTICE and upstream/TERMS.txt if the licence moved, and move the "
            "pin."
        ], True
    return ["- The Terms of Use are the pinned text."], False


# Each check, by the name the report gives it when it cannot finish.
CHECKS = (
    ("catalogue", check_catalogue),
    ("schema", check_schemas),
    ("archive", check_lines),
    ("terms of use", check_terms),
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--report", type=Path, help="Also write the Markdown report to this file"
    )
    args = parser.parse_args(argv)
    lines = [
        f"- Pinned edition: the CWE List {PINNED_EDITION} of {PINNED_DATE}, with "
        f"XSD {PINNED_XSD_VERSION}, {PINNED_SOURCE}."
    ]
    attention = False
    for label, check in CHECKS:
        try:
            found, needs = check()
        # OSError covers a refused or failed request and a timeout,
        # HTTPException and EOFError a connection cut off mid-answer,
        # ValueError an answer too large or of another shape, BadZipFile and
        # ParseError a file that is not what it should be.
        except (
            OSError,
            http.client.HTTPException,
            EOFError,
            ValueError,
            zipfile.BadZipFile,
            ET.ParseError,
        ) as err:
            found = [f"- **The {label} check could not finish: {_code(err)}.**"]
            needs = True
        lines += found
        attention = attention or needs
    text = "\n".join(lines) + "\n"
    print(text, end="")
    if args.report:
        args.report.write_text(text, encoding="utf-8")
    return 1 if attention else 0


if __name__ == "__main__":
    sys.exit(main())
