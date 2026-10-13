# Algorithms and Data Structures

Python coursework from the University of Alaska Anchorage: data structures and sorting from CSCE A311 (Spring 2024), and finite-state recognition from CSCE A351 (Fall 2025).

These notebooks preserve selected original code cells, including course scaffolding. They show completed classroom work and experiments, with historical limitations documented below. Notebook outputs, execution metadata, installation cells and assignment handout prose have been removed. See [attribution](NOTICE.md), [source provenance](PROVENANCE.json) and the [engineering portfolio](https://github.com/legooz/engineering-portfolio).

| Topic | Notebook | What to explore |
| --- | --- | --- |
| Binary search trees | [Movie BST](data-structures/movie-bst.ipynb) | Insertion, ordered traversal and deletion by movie rating; Graphviz display |
| Hash tables | [Chained hash table](data-structures/hash-tables.ipynb) | Collisions, retrieval and updating an existing key |
| Heaps | [Max heap](data-structures/heaps.ipynb) | Building a heap, insertion and maximum extraction |
| Linked lists | [List operations](data-structures/linked-list-operations.ipynb) | Insertion, finding and removing nodes |
| Sorting experiments | [Comparison sorting](sorting/comparison-sorting.ipynb) | Early termination, comparison counts and input size plots |
| Insertion sort | [Python insertion sort](sorting/insertion-sort.ipynb) | In-place insertion sort |
| Finite automata | [DFA URL recognizer](automata/dfa-url-recognizer.ipynb) | Explicit character transitions and accepting states |
| Regular expressions | [Regex URL recognizer](automata/regex-url-recognizer.ipynb) | Comparing a pattern-based recognizer with the DFA approach |

The C++ algorithms from the same course already live in [c-cpp-portfolio](https://github.com/legooz/c-cpp-portfolio): playlist reversal and shuffling, queues, priority queues, linked lists, sorting and binary trees. That repository includes their reviewed implementations and CMake checks.

## Running

Use Python 3.10 or later (the DFA uses `match`), and a Jupyter-compatible editor. Install dependencies in a virtual environment:

```sh
python -m venv .venv
# Activate the environment for your shell, then:
python -m pip install -r requirements.txt
```

Run notebook cells in order. The heap demonstration imports `copy`, which its class uses. The movie-tree demonstration additionally needs the Graphviz `dot` executable; its original `render(..., view=True)` call creates a file and opens a viewer. The automated checks load the tree class without running the display demo.

```sh
python -m unittest discover -s tests -v
```

## Validation and limits

The tests cover heap ordering, hash collisions and replacement, BST leaf/one-child/two-child deletion, linked-list removal, sorting edge cases, and recognizer examples. All eight notebooks also undergo schema and Python syntax checks. Test results characterize the preserved code; they do not imply exhaustive algorithm verification.

The DFA is a historical classroom recognizer, with permissive URL-prefix and IPv4 handling. The regex also covers only the demonstration's simplified URL forms. Neither is suitable as a general URL validator. The comparison notebook intentionally redefines sorting functions as it explores different variants. Original implementations have not been silently repaired during publication.

## Attribution

Course templates, demonstrations and starter code are part of these submissions. Their exact line-by-line authorship is not established. The BST deletion and sorting experiments appear within those teaching materials. Credits present in the source are retained, and no repository-wide license is asserted over instructor material. The recovery, organization and validation were assisted by AI in October 2026.
