import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main import prim_mst

class TestPrimMST(unittest.TestCase):
    def test_small_graph(self):
        graph = [
            [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]
        ]
        self.assertEqual(prim_mst(graph), 16)

    def test_triangle(self):
        graph = [
            [0, 1, 2],
            [1, 0, 3],
            [2, 3, 0]
        ]
        self.assertEqual(prim_mst(graph), 3)



    def test_single_node(self):
        graph = [[0]]
        self.assertEqual(prim_mst(graph), 0)

if __name__ == '__main__':
    unittest.main()
