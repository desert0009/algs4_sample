"""
253. Meeting Rooms II

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of conference rooms required.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1
 
Constraints:

1 <= intervals.length <= 104
"""

'''
# Priority Queue
Time: O(NlogN), Space: O(N)
'''

import heapq
import unittest

def metting_rooms(intervals):
    intervals.sort(key=lambda x: x[0]) # sort by start time
    q = [intervals[0][1]]
    for s, e in intervals[1:]:
        if s < q[0]: # q[0] = min(q)
            heapq.heappush(q, e)
        else:
            heapq.heapreplace(q, e) # replace the (min of q) with e
    return len(q)

class TestCase(unittest.TestCase):
    def test_1(self):
        intervals = [[0,30],[5,10],[15,20]]
        self.assertEqual(metting_rooms(intervals), 2)
    
    def test_2(self):
        intervals = [[7,10],[2,4]]
        self.assertEqual(metting_rooms(intervals), 1)


if __name__ == '__main__':
    unittest.main()

