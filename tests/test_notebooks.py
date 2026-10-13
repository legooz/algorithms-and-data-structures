"""Behavior checks for preserved coursework; never executes installation/viewer cells."""
from pathlib import Path
import ast
import contextlib
import copy
import io
import json
import unittest
import nbformat
import matplotlib

matplotlib.use("Agg")

ROOT = Path(__file__).resolve().parents[1]


def load(relative, indexes=None):
    notebook = json.loads((ROOT / relative).read_text(encoding="utf-8"))
    cells = ["".join(c["source"]) for c in notebook["cells"] if c["cell_type"] == "code"]
    namespace = {"__name__": "coursework_validation", "copy": copy}
    with contextlib.redirect_stdout(io.StringIO()):
        for i in (range(len(cells)) if indexes is None else indexes):
            exec(compile(cells[i], relative, "exec"), namespace)
    return namespace


class NotebookChecks(unittest.TestCase):
    def test_clean_notebook_schema_and_syntax(self):
        notebooks = list(ROOT.glob("*/*.ipynb"))
        self.assertEqual(len(notebooks), 8)
        for path in notebooks:
            with self.subTest(notebook=path.name):
                notebook = nbformat.read(path, as_version=4)
                nbformat.validate(notebook)
                for cell in notebook.cells:
                    if cell.cell_type == "code":
                        self.assertEqual(cell.outputs, [])
                        self.assertIsNone(cell.execution_count)
                        ast.parse(cell.source)

    def test_heap_extraction_is_descending_and_empty_is_safe(self):
        cls = load("data-structures/heaps.ipynb")["Heap"]
        for values in [[], [1], [5, 1, 5, -3, 0], list(range(20))]:
            heap = cls()
            heap.buildHeap(values)
            heap.insert(8)
            self.assertEqual([heap.extractMax() for _ in range(len(values) + 1)], sorted(values + [8], reverse=True))
            self.assertIsNone(heap.extractMax())

    def test_hash_collision_and_update(self):
        cls = load("data-structures/hash-tables.ipynb")["HashTable"]
        table = cls(1)
        table.add("first", 1)
        table.add("second", 2)
        table.add("first", 3)
        self.assertEqual(table.retrieve("first"), 3)
        self.assertEqual(table.retrieve("second"), 2)
        self.assertIsNone(table.retrieve("missing"))
        self.assertEqual(len(table.array[0]), 2)

    def test_bst_deletion_cases(self):
        cls = load("data-structures/movie-bst.ipynb", [0])["BinarySearchTree"]
        for deletion in [1, 3, 4, 5, 9]:
            tree = cls()
            values = [4, 2, 5, 1, 3, 6]
            for value in values:
                tree.insert({"title": str(value), "rating": value})
            tree.delete(deletion)
            self.assertEqual([m["rating"] for m in tree.inorder_traversal()], sorted(v for v in values if v != deletion))
            self.assertIn("digraph", tree.visualize().source)

    def test_linked_list_find_and_delete_second(self):
        cls = load("data-structures/linked-list-operations.ipynb")["LinkedList"]
        linked = cls()
        linked.deleteSecond()
        linked.insert(1)
        linked.deleteSecond()
        linked.insert(2)
        linked.insert(3)
        linked.deleteSecond()
        self.assertEqual(linked.head.info, 3)
        self.assertEqual(linked.head.next.info, 1)
        self.assertIsNone(linked.find(2))
        self.assertEqual(linked.find(1).info, 1)

    def test_insertion_and_comparison_sort(self):
        sorters = [load("sorting/insertion-sort.ipynb")["insertion_sort"]]
        # Select the completed early-exit and comparison-count variants.
        comparison = load("sorting/comparison-sorting.ipynb", [2, 6, 9])
        sorters.extend([comparison["bubbleSort"], comparison["selectionSort"]])
        for sorter in sorters:
            for values in [[], [1], [3, -1, 3, 0], list(range(8)), list(range(8, 0, -1))]:
                data = values.copy()
                with contextlib.redirect_stdout(io.StringIO()):
                    sorter(data)
                self.assertEqual(data, sorted(values))

    def test_dfa_basic_examples(self):
        ns = load("automata/dfa_exercises.ipynb")
        for token, accepted in [("https://example.org/x", True), ("example.org", True), ("user@example.org", False), ("ordinary", False)]:
            ns["octet"] = ""
            self.assertEqual(ns["run_dfa"](ns["START"], ns["accepts"], " " + token + " "), accepted)

    def test_regex_example_excludes_mail_and_invalid_ip(self):
        ns = load("automata/regular_expressions.ipynb")
        self.assertIn("alaska.org/automata", ns["result"])
        self.assertTrue(any(s.startswith("https://") for s in ns["result"]))
        self.assertFalse(any("@" in s or s.startswith("999.") for s in ns["result"]))


if __name__ == "__main__":
    unittest.main()
