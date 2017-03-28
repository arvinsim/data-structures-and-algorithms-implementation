import unittest

def selection_sort(integer_list):
    """
    The selection sort improves on the bubble sort by making only one exchange for every pass 
    through the list. In order to do this, a selection sort looks for the largest value as it makes 
    a pass and, after completing the pass, places it in the proper location. As with a bubble sort, 
    after the first pass, the largest item is in the correct place. After the second pass, the next 
    largest is in place. This process continues and requires n−1n−1 passes to sort n items, since 
    the final item must be in place after the (n−1)(n−1) st pass.

    This implementation starts from the end of the list

    integer_list -- A list of integers
    """
    for index in range(len(integer_list)-1, 1, -1):
        largest_index = index
        for i in range(index):
            if integer_list[i] > integer_list[largest_index]:
                largest_index = i
        # Swap largest value with current index
        integer_list[largest_index], integer_list[index] = \
        integer_list[index], integer_list[largest_index]
    return integer_list


class TestSelectionSort(unittest.TestCase):
    """Unit tests for selection sort function"""

    def test_bubble_sort(self):
        """Selection Sort tests"""
        self.assertEqual(
            selection_sort([5, 4, 3, 2, 1]),
            [1, 2, 3, 4, 5]
        )
        self.assertEqual(
            selection_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]),
            [17, 20, 26, 31, 44, 54, 55, 77, 93]
        )

if __name__ == '__main__':
    unittest.main()
