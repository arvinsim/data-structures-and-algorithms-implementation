import unittest

def insertion_sort(l):
    """
    The insertion sort, although still O(n^2), works in a slightly different way. It always 
    maintains a sorted sublist in the lower positions of the list. Each new item is then "inserted" 
    back into the previous sublist such that the sorted sublist is one item larger.
    """
    for index in range(1, len(l)):
        currentvalue = l[index]
        position = index

        while position > 0 and l[position-1] > currentvalue:
            l[position] = l[position-1]
            position -= 1

        l[position] = currentvalue
    return l

class TestInsertionSort(unittest.TestCase):
    """Unit tests for insertion sort function"""

    def test_insertion_sort(self):
        """Insertion Sort tests"""
        self.assertEqual(
            insertion_sort([5, 4, 3, 2, 1]),
            [1, 2, 3, 4, 5]
        )
        self.assertEqual(
            insertion_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]),
            [17, 20, 26, 31, 44, 54, 55, 77, 93]
        )

if __name__ == '__main__':
    unittest.main()
