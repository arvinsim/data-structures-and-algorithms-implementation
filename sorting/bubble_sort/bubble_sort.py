import unittest


def bubble_sort(integer_list):
    """
    An implementation of bubble sort

    If there are n items in the list, then there are n-1 pairs of items that need to be compared 
    on the first pass. It is important to note that once the largest value in the list is part of a 
    pair, it will continually be moved along until the pass is complete. At the start of the second 
    pass, the largest value is now in place.

    Start
    [3,2,1]

    First Pass
    [2,3,1]
    [2,1,3]

    Second Pass
    [1,2,3]

    Done
    

    l - list of integers
    """
    for passnum in range(len(integer_list), 1, -1):
        for i in range(passnum-1):
            if integer_list[i] > integer_list[i+1]:
                integer_list[i], integer_list[i+1] = integer_list[i+1], integer_list[i]
    return integer_list


def short_bubble_sort(integer_list):
    """
    This implementation is just the same as the normal bubble sort but it can recognize
    that the list is sorted if no exchanges are made in one pass
    """
    exchanged = True
    for passnum in range(len(integer_list), 1, -1):
        exchanged = False
        for i in range(passnum-1):
            if integer_list[i] > integer_list[i+1]:
                exchanged = True
                integer_list[i], integer_list[i+1] = integer_list[i+1], integer_list[i]
        if not exchanged:
            break
    return integer_list


class TestBubbleSort(unittest.TestCase):
    """Unit tests for bubble sort function"""

    def test_bubble_sort(self):
        """Bubble Sort tests"""
        self.assertEqual(
            bubble_sort([5, 4, 3, 2, 1]),
            [1, 2, 3, 4, 5]
        )
        self.assertEqual(
            bubble_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]),
            [17, 20, 26, 31, 44, 54, 55, 77, 93]
        )

    def test_short_bubble_sort(self):
        """Short Bubble Sort tests"""
        self.assertEqual(
            short_bubble_sort([5, 4, 3, 2, 1]),
            [1, 2, 3, 4, 5]
        )
        self.assertEqual(
            short_bubble_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]),
            [17, 20, 26, 31, 44, 54, 55, 77, 93]
        )
if __name__ == '__main__':
    unittest.main()
