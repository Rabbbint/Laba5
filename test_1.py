import unittest
from one import longest_common_prefix


class TestLongestCommonPrefix(unittest.TestCase):
    def test_common_prefix(self):
        self.assertEqual(longest_common_prefix(
            ["перемена", "передел", "перестройка"]), "пере")
        self.assertEqual(longest_common_prefix(["ффф", "ппп", "ааа"]), "")
        self.assertEqual(longest_common_prefix(["1", "2", "3"]), "")
        self.assertEqual(longest_common_prefix(["-", "-", "+"]), "")


if __name__ == '__main__':
    unittest.main()