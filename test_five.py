import unittest
from five import fibonacci


class TestFibonaci(unittest.TestCase):
    def test_fibonaci(self):
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(8), 21)


if __name__ == '__main__':
    unittest.main()