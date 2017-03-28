import unittest

def merge(left, right):
    """
    Function to merge two lists
    """
    merged = []
    # Merge until one list becomes empty
    while left and right:
        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    if len(left) == 0:
        merged += right
    else:
        merged += left
    return merged

def merge_sort(integer_list):
    """
    The main merge sort function
    """
    if len(integer_list) < 2:
        return integer_list
    else:
        mid = len(integer_list) // 2
        left = merge_sort(integer_list[:mid])
        right = merge_sort(integer_list[mid:])
        return merge(left, right)


class TestMergeSort(unittest.TestCase):
    """Unit tests for merge sort function"""

    def test_merge_sort(self):
        """Merge Sort tests"""
        self.assertEqual(
            merge_sort([5, 4, 3, 2, 1]),
            [1, 2, 3, 4, 5]
        )
        self.assertEqual(
            merge_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]),
            [17, 20, 26, 31, 44, 54, 55, 77, 93]
        )

if __name__ == '__main__':
    unittest.main()
