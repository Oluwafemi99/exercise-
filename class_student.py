import unittest

def square(x):
    p = x * x
    return p

class valueNotAccepted(Exception):
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return f"sorry invalid no"
    
"""
def main():
    try:
        x = int(input("enter a no"))
        result = square(x)
        if x == 0:
            raise valueNotAccepted(x)
    except valueNotAccepted as e:
        print(e)
    else:
        print(result)
"""

class testsquare(unittest.TestCase):
    def test_square_valid(self):
        self.assertEqual(square(4), 16)
        self.assertEqual(square(10), 100)

    def test_sqare_invalid(self):
        with self.assertRaises(valueNotAccepted):
            if 0:
                raise valueNotAccepted
            
unittest.main()
        