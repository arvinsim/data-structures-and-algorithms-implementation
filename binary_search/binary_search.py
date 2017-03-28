import unittest

def binary_search(i, l):
    """
    Checks if an item exist in a list using a non-recursive implementation of binary search

    i -- item to search for
    l -- item to search in 
    """
    first = 0
    last = len(l) - 1
    found = False

    while first <= last and found is False:
        midpoint = (first + last) // 2
        if l[midpoint] == i:
            return True
        else:
            if i < l[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1


# Tests
class TestBinarySearch(unittest.TestCase):
    def test_odd(self):
        self.assertEqual(
            binary_search(9, [1, 3, 5, 7, 9]),
            True
        )

    def test_even(self):
        self.assertEqual(
            binary_search(4, [2, 4, 6, 8, 10, 12]),
            True
        )

if __name__ == '__main__':
    unittest.main()