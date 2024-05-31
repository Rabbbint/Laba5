import unittest
from two import roman_to_arabic


class TestRomanToArabic(unittest.TestCase):
    def test_common_prefix(self):
        self.assertEqual(roman_to_arabic("CLIV"), 154)
        self.assertEqual(roman_to_arabic("XI"), 11)


if __name__ == '__main__':
    unittest.main()