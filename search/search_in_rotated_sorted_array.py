"""
33. Search in Rotated Sorted Array

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1
 
Constraints:
1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
All values of nums are unique.
nums is guaranteed to be rotated at some pivot.
-10^4 <= target <= 10^4
"""
import unittest

def serach(nums, target):
    # Input: nums = [4,5,6,7,0,1,2], target = 0
    # Output: 4
    l, r = 0, len(nums) - 1
    while l < r:
        m = (l + r) // 2
        if nums[target] == m:
            return m
        elif nums[m] < nums[r]: # right-sorted
            if nums[m] <= target <= nums[r]:
                l = m + 1
            else:
                r = m - 1
        else: # left-sorted
            if nums[l] <= target <= nums[m]:
                r = m - 1
            else:
                l = m + 1
    return l if nums[l] == target else -1 # r == l

class TestCase(unittest.TestCase):
    def test_1(self):
        nums = [4,5,6,7,0,1,2]
        self.assertEqual(serach(nums, 0), 4)
    
    def test_2(self):
        nums = [4,5,6,7,0,1,2]
        self.assertEqual(serach(nums, 3), -1)
    
    def test_3(self):
        nums = [1]
        self.assertEqual(serach(nums, 0), -1)
    
    def test_4(self):
        nums = [3,4,5,6,1,2]
        self.assertEqual(serach(nums, 2), 5)

if __name__ == '__main__':
    unittest.main()