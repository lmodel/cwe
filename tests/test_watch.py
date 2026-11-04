"""Checks the upstream watch's decisions against stubbed answers.

scripts/check_upstream_release.py reads MITRE's public pages. These tests replace
its one network call, `_get`, with a table of answers, so they run offline. They
show what the report says in each case the watch knows: another edition, changed
bytes under the same edition, a changed XSD, the "latest" link fixed or moved, a
new schema on the archive page, changed terms, and a check that could not finish.
"""

import http.client
import importlib.util
import io
import urllib.error
import zipfile
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "check_upstream_release.py"
UPSTREAM = ROOT / "upstream"


@pytest.fixture
def watch():
    """A fresh copy of the script, so no test sees another's stub."""
    spec = importlib.util.spec_from_file_location("watch_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _zip(xml):
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as archive:
        archive.writestr("cwec_v9.9.xml", xml)
    return buffer.getvalue()


def _terms_page(text):
    return f"<html><p>{text}</p><b>Page Last Updated: </b></html>".encode()


def _not_found(url):
    return urllib.error.HTTPError(url, 404, "Not Found", None, None)


def _answers(watch):
    """The answers of an unchanged upstream, with the parts a test changes."""
    return {
        watch.CATALOGUE_URL: (UPSTREAM / "cwec_v5.0.xml.zip").read_bytes(),
        watch.PINNED_SOURCE: (UPSTREAM / "cwe_schema_v8.0.xsd").read_bytes(),
        watch.LATEST_XSD_URL: b"the earlier copy",
        watch.ARCHIVE_URL: (
            b'<a href="/data/xsd/cwe_schema_v8.0.xsd">XSD</a>'
            b'<a href="/data/xsd/cwe_schema_v7.4.xsd">XSD</a>'
            b'<a href="/data/xsd/cwe_schema_v7.3.xsd">XSD</a>'
        ),
        watch.TERMS_URL: _page_of_the_terms(watch),
    }


def _page_of_the_terms(watch):
    """The page that gives back upstream/TERMS.txt, in the markup MITRE uses."""
    held = (UPSTREAM / "TERMS.txt").read_text(encoding="utf-8")
    body = held.replace("CWE™", watch.TERMS_START.split(" ")[0], 1)
    paragraphs = "".join(f"<p>{line}</p>" for line in body.split("\n\n"))
    return f"<html><h1>Terms</h1>{paragraphs}{watch.TERMS_END}</html>".encode()


def _stub(watch, answers):
    """Make `_get` answer from the table, an exception being raised, and pin the
    file behind the "latest" link to the table's bytes."""

    def get(url):
        answer = answers[url]
        if isinstance(answer, Exception):
            raise answer
        return answer

    watch._get = get
    watch.PINNED_LATEST_XSD_BLOB = watch.blob(b"the earlier copy")


def _run(watch, tmp_path):
    report = tmp_path / "report.md"
    code = watch.main(["--report", str(report)])
    return code, report.read_text(encoding="utf-8")


def test_nothing_changed(watch, tmp_path):
    """With the pinned edition, schema, archive and terms, the watch exits 0."""
    _stub(watch, _answers(watch))
    code, text = _run(watch, tmp_path)
    assert code == 0, text
    assert "The latest CWE List is the pinned edition, 5.0." in text
    assert "XSD 8.0 is the pinned file." in text
    assert "still holds an earlier copy of XSD 8.0, as pinned." in text
    assert "lists no schema beyond 8.0 and 7.4." in text
    assert "The Terms of Use are the pinned text." in text


def test_another_edition(watch, tmp_path):
    """A latest catalogue of another version needs attention."""
    answers = _answers(watch)
    answers[watch.CATALOGUE_URL] = _zip(
        '<Weakness_Catalog Name="CWE" Version="5.1" Date="2027-01-30"/>'
    )
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**The latest CWE List is version `5.1` of `2027-01-30`;" in text


def test_other_bytes_under_the_same_edition(watch, tmp_path):
    """The same version and date with other XML needs attention."""
    answers = _answers(watch)
    answers[watch.CATALOGUE_URL] = _zip(
        '<Weakness_Catalog Name="CWE" Version="5.0" Date="2026-10-28"/>'
    )
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**The XML of CWE 5.0 changed under the same version.**" in text


def test_a_changed_versioned_schema(watch, tmp_path):
    answers = _answers(watch)
    answers[watch.PINNED_SOURCE] = b"another schema"
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert f"**{watch.PINNED_SOURCE} changed.**" in text


def test_the_latest_link_fixed(watch, tmp_path):
    """MITRE fixing the mismatch needs a person, who drops the pin and the docs."""
    answers = _answers(watch)
    answers[watch.LATEST_XSD_URL] = answers[watch.PINNED_SOURCE]
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "now holds the same file as XSD 8.0.**" in text


def test_the_latest_link_moved(watch, tmp_path):
    answers = _answers(watch)
    answers[watch.LATEST_XSD_URL] = b"something new"
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "changed, and is not XSD 8.0.**" in text


def test_a_newer_schema_on_the_archive_page(watch, tmp_path):
    answers = _answers(watch)
    answers[watch.ARCHIVE_URL] += b'<a href="/data/xsd/cwe_schema_v8.1.xsd">XSD</a>'
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**The archive page lists a newer schema: `8.1`.**" in text


def test_a_newer_parallel_schema_is_for_information(watch, tmp_path):
    """The parallel line moving asks for nobody, because the schema does not render it."""
    answers = _answers(watch)
    answers[watch.ARCHIVE_URL] += b'<a href="/data/xsd/cwe_schema_v7.5.xsd">XSD</a>'
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 0, text
    assert "For information, the parallel 4.x line has moved to schema `7.5`." in text


def test_the_archive_drops_the_pinned_schema(watch, tmp_path):
    answers = _answers(watch)
    answers[watch.ARCHIVE_URL] = b"no schema here"
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**The archive page no longer lists XSD 8.0.**" in text


def test_the_terms_changed(watch, tmp_path):
    answers = _answers(watch)
    answers[watch.TERMS_URL] = _terms_page(f"{watch.TERMS_START} a new licence.")
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**The Terms of Use changed at" in text


def test_the_terms_page_of_another_shape_could_not_finish(watch, tmp_path):
    answers = _answers(watch)
    answers[watch.TERMS_URL] = b"<html>moved</html>"
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**The terms of use check could not finish: `the Terms of Use page" in text


@pytest.mark.parametrize(
    ("failure", "shown"),
    [
        (_not_found("https://cwe.mitre.org/x"), "`HTTP Error 404: Not Found`"),
        (urllib.error.URLError("refused"), "`<urlopen error refused>`"),
        (TimeoutError("timed out"), "`timed out`"),
        (http.client.IncompleteRead(b"x"), "`IncompleteRead(1 bytes read)`"),
        (ValueError("too large"), "`too large`"),
    ],
)
def test_a_check_that_could_not_finish(watch, tmp_path, failure, shown):
    """A refused, failed, cut-off or oversized answer stops one check, says so,
    and leaves the other checks to run and the report to be written."""
    answers = _answers(watch)
    answers[watch.CATALOGUE_URL] = failure
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert f"**The catalogue check could not finish: {shown}" in text
    assert "The Terms of Use are the pinned text." in text


def test_a_file_that_is_not_a_zip_could_not_finish(watch, tmp_path):
    answers = _answers(watch)
    answers[watch.CATALOGUE_URL] = b"not a zip"
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**The catalogue check could not finish: `File is not a zip file`.**" in text


def test_xml_that_does_not_parse_could_not_finish(watch, tmp_path):
    answers = _answers(watch)
    answers[watch.CATALOGUE_URL] = _zip("not xml")
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**The catalogue check could not finish: `syntax error" in text


def test_a_zip_of_two_files_could_not_finish(watch, tmp_path):
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as archive:
        archive.writestr("a.xml", "<a/>")
        archive.writestr("b.xml", "<b/>")
    answers = _answers(watch)
    answers[watch.CATALOGUE_URL] = buffer.getvalue()
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "the ZIP holds 2 XML files, not one" in text


def test_text_the_server_chose_is_quoted_on_one_line(watch, tmp_path):
    """A version with a blank line, a mention and a backtick stays inside its
    code span, so the issue mentions no one."""
    answers = _answers(watch)
    answers[watch.CATALOGUE_URL] = _zip(
        '<Weakness_Catalog Version="9&#10;&#10;@someone `x`" Date="2027-01-30"/>'
    )
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "version `9 @someone 'x'` of `2027-01-30`;" in text


class _Answer:
    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def read(self, size):
        return b"{}"


def test_no_token_travels(watch, monkeypatch):
    """The watch sends no token: the pages are public and the host is not GitHub."""
    monkeypatch.setenv("GITHUB_TOKEN", "not-to-send")
    sent = {}

    def urlopen(req, timeout):
        sent["headers"] = dict(req.header_items())
        sent["unredirected"] = dict(req.unredirected_hdrs)
        return _Answer()

    monkeypatch.setattr(watch, "_open", urlopen)
    watch._get(watch.TERMS_URL)
    assert sent["headers"]["User-agent"] == "lmodel-cwe-watch"
    assert "Authorization" not in sent["headers"]
    assert not sent["unredirected"]


def test_an_answer_over_the_cap_is_refused(watch, monkeypatch):
    """An answer larger than MAX_BYTES raises rather than being read whole."""

    class Big(_Answer):
        def read(self, size):
            return b"x" * size

    monkeypatch.setattr(watch, "_open", lambda req, timeout: Big())
    with pytest.raises(ValueError, match="larger than"):
        watch._get(watch.TERMS_URL)


def test_a_redirect_off_the_expected_host_is_refused(watch):
    """A redirect is followed over https to cwe.mitre.org, and nowhere else."""
    handlers = watch._open.__self__.handlers
    assert any(isinstance(h, watch._ExpectedHostRedirect) for h in handlers)
    handler = watch._ExpectedHostRedirect()
    req = watch.urllib.request.Request(watch.TERMS_URL)
    for newurl in (
        "https://example.org/about/termsofuse.html",
        "http://cwe.mitre.org/about/termsofuse.html",
        "https://cwe.mitre.org.example.org/about/termsofuse.html",
    ):
        with pytest.raises(ValueError, match="leads off the expected hosts"):
            handler.redirect_request(req, None, 302, "Found", {}, newurl)
    moved = "https://cwe.mitre.org/about/terms.html"
    assert (
        handler.redirect_request(req, None, 301, "Moved", {}, moved).full_url == moved
    )


def test_the_terms_text_is_what_upstream_holds(watch):
    """Reading a page in MITRE's markup gives back the pinned text."""
    assert watch.terms_text(_page_of_the_terms(watch)) == (
        UPSTREAM / "TERMS.txt"
    ).read_text(encoding="utf-8")
