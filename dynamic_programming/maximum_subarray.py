"""
Maximum Subarray

Given an integer array nums, 
find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
 
Constraints:
1 <= nums.length <= 3 * 10^4
-10^5 <= nums[i] <= 10^5
"""

'''
    [-2,1,-3,4,-1,2,1,-5,4]
dp   -2 1 -2 4  3 5 6 1  5
ans  -2 1 1  4  4 5 6 6  6
'''
import unittest

def maxSubArray(nums):
    dp = nums[0]
    ans = dp
    for n in nums[1:]:
        dp = max(dp + n, n)
        ans = max(ans, dp)
    return ans

class TestCase(unittest.TestCase):
    def test_1(self):
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        self.assertEqual(maxSubArray(nums), 6)
    
    def test_2(self):
        nums = [1]
        self.assertEqual(maxSubArray(nums), 1)
    
    def test_3(self):
        nums = [5,4,-1,7,8]
        self.assertEqual(maxSubArray(nums), 23)

if __name__ == '__main__':
    unittest.main()