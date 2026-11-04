# Example data for cwe

- `valid/` holds an example of each class. Most are real pieces of the CWE List 5.0, each naming the entry it comes from, and the tree root is written by hand so that its references resolve. `linkml-run-examples` and `tests/test_data.py` read this folder.
- `invalid/` holds a counter-example for each constraint the validator can state. Each file's first line, `# Fails at: <JSON pointer>`, names its one failing place, and `tests/test_data.py` holds it there.
- `problem/invalid/` holds a counter-example for each rule the generated JSON Schema cannot state, which `tests/cwe_rules.py` checks over a whole catalogue.

A file name is `ClassName-anything.yaml`, and the class is the part before the first hyphen. The whole catalogue is under `upstream/`, and `tests/test_catalogue.py` validates it.

The real pieces are copies under MITRE's Terms of Use: Copyright (c) 2006-2026, The MITRE Corporation. See [NOTICE](../../NOTICE).
