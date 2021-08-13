"""
75. Sort Colors (Medium)

Given an array nums with n objects colored red, white, or blue, 
sort them ### in-place #### so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""

"""
[QuickSort]
    Time: worst case: O(N^2), average case O(NlogN), best case O(NlogN)
    Space: O(1)
    In-place

[With Freq Dic]
    Time: O(2N) -> O(N)
    Space: O(3) -> O(1)
    In-place
"""

import unittest

def sort_color(nums):
    freq = {0: 0, 1: 0, 2: 0}
    for n in nums:
        freq[n] += 1

    sum_cnt = 0
    for key in freq:
        cnt = freq[key]
        for i in range(sum_cnt, sum_cnt + cnt):
            nums[i] = key
        sum_cnt += cnt

class TestCase(unittest.TestCase):
    def test_1(self):
        nums = [2,0,2,1,1,0]
        sort_color(nums)
        self.assertEqual(nums, [0,0,1,1,2,2])
    
    def test_2(self):
        nums = [2,0,1]
        sort_color(nums)
        self.assertEqual(nums, [0,1,2])
    
    def test_3(self):
        nums = [0]
        sort_color(nums)
        self.assertEqual(nums, [0])

    def test_4(self):
        nums = [1]
        sort_color(nums)
        self.assertEqual(nums, [1])

if __name__ == '__main__':
    unittest.main()