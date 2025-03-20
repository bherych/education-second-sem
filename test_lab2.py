import unittest
import lab2

class Lab_Test(unittest.TestCase):
    
    def test_max_hamsters(self):
         
         self.assertEqual(lab2.max_hamsters(7, [[1, 2], [2, 2], [3, 1]]), 2)
         self.assertEqual(lab2.max_hamsters(19, [[5, 0], [2, 2], [1, 4], [5, 1]]), 3)
         self.assertEqual(lab2.max_hamsters(2, [[1, 50000], [1, 60000]]), 1)
         


if __name__ == '__main__':
     unittest.main()