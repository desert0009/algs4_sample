"""
Merge Sort Implement

Time: O(NlogN)
Space: O(N)
Stable
"""
import unittest

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    m = len(nums) // 2
    left = merge_sort(nums[:m])
    right = merge_sort(nums[m:])
    return merge(left, right)

def merge(left, right):
    i, j = 0, 0
    m, n = len(left), len(right)
    res = []
    while i < m and j < n:
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res

class TestCase(unittest.TestCase):
    def test_1(self):
        nums = [1, 5, 3, 2, 8, 7, 6, 4]
        self.assertEqual(merge_sort(nums), [1, 2, 3, 4, 5, 6, 7, 8])
    
    def test_2(self):
        nums = [2, 1]
        self.assertEqual(merge_sort(nums), [1, 2])
    
    def test_3(self):
        nums = []
        self.assertEqual(merge_sort(nums), [])

if __name__ == '__main__':
    unittest.main()