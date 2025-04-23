import unittest
from node import BinaryTree
import main

class Lab_Test(unittest.TestCase):
    
    def test_find_successor(self):
        root = BinaryTree(10)
        node5 = BinaryTree(5, parent=root)
        node15 = BinaryTree(15, parent=root)
        node3 = BinaryTree(3, parent=node5)
        node7 = BinaryTree(7, parent=node5)
        node12 = BinaryTree(12, parent=node7)
        node20 = BinaryTree(20, parent=node15)

        root.left = node5
        root.right = node15
        node5.left = node3
        node5.right = node7
        node7.left = node12
        node15.right = node20

        self.assertEqual(main.find_successor(root, node3).value, 5)
        self.assertEqual(main.find_successor(root, node5).value, 12)
        self.assertEqual(main.find_successor(root, node12).value, 7)
        self.assertEqual(main.find_successor(root, node7).value, 10)
        self.assertEqual(main.find_successor(root, root).value, 15)
        self.assertEqual(main.find_successor(root, node15).value, 20)
        self.assertEqual(main.find_successor(root, node20).value, None)

if __name__ == '__main__':
     unittest.main()