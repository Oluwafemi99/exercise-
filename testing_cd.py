# testing in python
# test the sqaure of a no

import unittest


def square(x):
    p = x * x
    return p


# module for the testings


class TestOperation(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(2), 4)


unittest.main()
