import unittest
from four import is_alphabetical


class TestCheckAnagrams(unittest.TestCase):
    def test_anagrams(self):
        self.assertTrue(is_alphabetical(["listen", "silent"]))
        self.assertTrue(is_alphabetical(["hello", "llohe"]))
        self.assertFalse(is_alphabetical(["apple", "orange"]))


if __name__ == '__main__':
    unittest.main()