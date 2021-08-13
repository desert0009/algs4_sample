"""
Quick Sort Implement
"""

"""
Time: worst case: O(N^2), average case O(NlogN), best case O(NlogN)
Space: O(1)
In-place

Shuffle list before QuickSort to avoid the time worst case O(N^2)
"""
import unittest
import random

def quick_sort(nums, l, r):
    if l >= r:
        return
    p = partition(nums, l, r)
    quick_sort(nums, l, p - 1)
    quick_sort(nums, p + 1, r)

def partition(nums, l, r):
    pivot = nums[r]
    i = l
    for j in range(l, r):
        if nums[j] < pivot:
            swap(nums, i, j)
            i += 1
    swap(nums, i, r)
    return i

def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]

class TestCase(unittest.TestCase):
    def test_1(self):
        nums = [1, 5, 3, 2, 8, 7, 6, 4]
        random.shuffle(nums)
        quick_sort(nums, 0, len(nums) - 1)
        self.assertEqual(nums, [1, 2, 3, 4, 5, 6, 7, 8])
    
    def test_2(self):
        nums = [2, 1]
        random.shuffle(nums)
        quick_sort(nums, 0, len(nums) - 1)
        self.assertEqual(nums, [1, 2])
    
    def test_3(self):
        nums = []
        random.shuffle(nums)
        quick_sort(nums, 0, len(nums) - 1)
        self.assertEqual(nums, [])

if __name__ == '__main__':
    unittest.main()