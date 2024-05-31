import unittest
from three import roman_to_arabic


class TestRomanToArabic(unittest.TestCase):
    def test_common_prefix(self):
        self.assertEqual(roman_to_arabic("ддд"), "ошибка")
        self.assertEqual(roman_to_arabic("CLIV"), 154)
        self.assertEqual(roman_to_arabic("X"), 10)


if __name__ == '__main__':
    unittest.main()