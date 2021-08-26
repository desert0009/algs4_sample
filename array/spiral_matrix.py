"""
Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],
                 [4,5,6],
                 [7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

import unittest

def spiralOrder(matrix):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    _dir = 0
    m, n = len(matrix), len(matrix[0])
    visited = []
    ans = []
    i, j = 0, 0
    while len(ans) < (m * n):
        ans.append(matrix[i][j])
        visited.append((i, j))

        next_i = i + dirs[_dir][0]
        next_j = j + dirs[_dir][1]
        if next_i < 0 or next_j < 0 or next_i >= m or next_j >= n or (next_i, next_j) in visited:
            _dir = (_dir + 1) % 4
            next_i = i + dirs[_dir][0]
            next_j = j + dirs[_dir][1]
        i, j = next_i, next_j
    return ans

class TestCase(unittest.TestCase):
    def test_1(self):
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        self.assertEqual(spiralOrder(matrix), [1,2,3,6,9,8,7,4,5])
    
    def test_2(self):
        matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
        self.assertEqual(spiralOrder(matrix), [1,2,3,4,8,12,11,10,9,5,6,7])

if __name__ == '__main__':
    unittest.main()
