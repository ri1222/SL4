import unittest
from speciallecture.SortAlgorithm import SortAlgorithm

class TestSortAlgorithm(unittest.TestCase):
    
    def buggy_quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        left = [x for x in arr if x < pivot]
        center = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.buggy_quick_sort(left) + center + self.buggy_quick_sort(right)


    def test_sorted_list(self):
        sort = SortAlgorithm()
        self.assertEqual(sort.buggy_quick_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        sort = SortAlgorithm()
        self.assertEqual(sort.buggy_quick_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_negative_numbers(self):
        sort = SortAlgorithm()
        self.assertEqual(sort.buggy_quick_sort([-3, -1, -4, -2, -5]), [-5, -4, -3, -2, -1])

    def test_empty_list(self):
        sort = SortAlgorithm()
        self.assertEqual(sort.buggy_quick_sort([]), [])

    def test_duplicates(self):
        sort = SortAlgorithm()
        self.assertEqual(sort.buggy_quick_sort([2, 3, 2, 1]), [1, 2, 2, 3])

    def test_all_same(self):
        sort = SortAlgorithm()
        self.assertEqual(sort.buggy_quick_sort([5, 5, 5]), [5, 5, 5])
