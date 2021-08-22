"""
56. Merge Intervals (Medium)

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 
Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""
import unittest

def merge(intervals):
    if not intervals:
        return None
    intervals.sort(key=lambda x: x[0]) # sort by start
    ans = [intervals[0]]
    for i in range(1, len(intervals)):
        s, e = intervals[i]
        if s <= ans[-1][1]:
            ans[-1] = [min(s, ans[-1][0]), max(e, ans[-1][1])]
        else:
            ans.append(intervals[i])
    return ans

"""
Given sorted intervals. insert the item([start, end]) to intervals
"""
def insert(intervals, item):
    # Time: O(2N) -> O(N)
    # Space: O(N)
    N = len(intervals)
    dic = {-1: [], 0: [], 1: []}
    def get_tag(item1, item2):
        s1, e1 = item1
        s2, e2 = item2
        if s2 > e1:
            return -1
        elif s2 <= s1 <= e2 or s1 <= s2 <= e1:
            return 0
        else: # e2 < s1
            return 1
    for i in range(N):
        key = get_tag(intervals[i], item)
        dic[key].append(i)

    ans = []
    for i in dic[-1]:
        ans.append(intervals[i])
    if len(dic[0]) > 0:
        _start = min(item[0], intervals[dic[0][0]][0])
        _end = max(item[1], intervals[dic[0][-1]][1])
        ans.append([_start, _end])
    else:
        ans.append(item)
    for i in dic[1]:
        ans.append(intervals[i])
    return ans
    
class TestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(merge([[1,3],[2,6],[8,10],[15,18]]), [[1,6],[8,10],[15,18]])
    
    def test_2(self):
        self.assertEqual(merge([[1,4],[4,5]]), [[1,5]])
    
    def test_3(self):
        self.assertEqual(merge([[3, 5], [1, 2]]), [[1, 2], [3, 5]])
    
    def test_4(self):
        self.assertEqual(merge([[3, 5], [2, 7]]), [[2, 7]])

    ########
    def test_5(self):
        self.assertEqual(insert([[1,4], [7, 9]], [5, 6]), [[1,4], [5, 6], [7, 9]])
    
    def test_6(self):
        self.assertEqual(insert([[1,4], [7, 9], [10, 11], [16, 18]], [5, 15]), 
                                [[1,4], [5, 15], [16, 18]])
    
    def test_7(self):
        self.assertEqual(insert([[1,4], [7, 9], [10, 11], [16, 18]], [3, 15]), 
                                [[1, 15], [16, 18]])

if __name__ == '__main__':
    unittest.main()


