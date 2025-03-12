import unittest
import lab1

class TestZigZag(unittest.TestCase):

    def test_zigzag(self):
        self.assertEqual(lab1.zigzag([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 2, 4, 7, 5, 3, 6, 8, 9])
        self.assertEqual(lab1.zigzag([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]), [1, 2, 6, 11, 7, 3, 4, 8, 12, 16, 21, 17, 13, 9, 5, 10, 14, 18, 22, 23, 19, 15, 20, 24, 25])
        self.assertEqual(lab1.zigzag([[1, 2], [3, 4], [5, 6], [7, 8]]), [1, 2, 3, 5, 4, 6, 7, 8])
        self.assertEqual(lab1.zigzag([[1, 2, 3, 4, 5, 6]]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(lab1.zigzag([[1]]), [1])

if __name__ == '__main__':
    unittest.main()