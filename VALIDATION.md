# Validation record

Checked on October 12, 2026 with Python 3.13, graphviz 0.21, matplotlib 3.11.2 and nbformat 5.11.1.

`python -m unittest discover -s tests -v` passed all eight test groups:

- Eight notebook schemas, empty output arrays, null execution counts and Python syntax.
- Heap building/insertion/extraction over empty, singleton, duplicate, negative and ordered inputs.
- Colliding hash keys, replacement without duplicate keys and missing-key lookup.
- BST leaf, one-child, two-child and absent-rating deletion with ordered traversal.
- Empty/singleton list handling, finding nodes and second-node deletion.
- Insertion, bubble and selection sort over empty, singleton, duplicate, negative, sorted and reversed inputs.
- Basic accepted/rejected DFA examples.
- Regex sample results, excluding email and the invalid IPv4 example.

The plotting cell ran with a noninteractive backend; matplotlib reported that its figure could not be shown. Graphviz source generation was checked, but external Graphviz rendering and viewer launch were not run. Saved notebook output remains cleared. Source-file hashes were verified against PROVENANCE.json.

These are bounded checks of original coursework, not a claim that every recognizer form, edge case or algorithm variant is correct. Known limitations are described in README.md.
