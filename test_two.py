import unittest
from random import randint
from two import rand_list

class TestRandList(unittest.TestCase):

    def test_rand_list(self):
        a = [randint(0, 1001) for _ in range(10)]
        original_a = a.copy()
        deleted_num = rand_list(a)
        self.assertIn(deleted_num, original_a)
        self.assertEqual(len(a), len(original_a) - 1)

if __name__ == '__main__':
    unittest.main()
