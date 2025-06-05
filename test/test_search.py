import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from search import find_string

class TestFindString(unittest.TestCase):

    def test_single_occurrence(self):
        self.assertEqual(find_string("abcdef", "cd"), [2])

    def test_multiple_occurrences(self):
        self.assertEqual(find_string("abababab", "ab"), [0, 2, 4, 6])

    def test_no_occurrence(self):
        self.assertEqual(find_string("abcdefgh", "xyz"), [])

    def test_empty_needle(self):
        self.assertEqual(find_string("abc", ""), [])

    def test_empty_haystack(self):
        self.assertEqual(find_string("", "a"), [])

    def test_needle_longer_than_haystack(self):
        self.assertEqual(find_string("ab", "abc"), [])

    def test_full_match(self):
        self.assertEqual(find_string("hello", "hello"), [0])

    def test_overlap(self):
        self.assertEqual(find_string("aaaaa", "aaa"), [0, 1, 2])

    def test_special_characters(self):
        self.assertEqual(find_string("a$%^&a$%^&", "$%^&"), [1, 6])

if __name__ == '__main__':
    unittest.main()
