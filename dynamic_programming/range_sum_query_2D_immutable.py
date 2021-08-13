"""
304. Range Sum Query 2D - Immutable
"""
import unittest

class NumMatrix:
    def __init__(self, matrix):
        m, n = len(matrix), len(matrix[0])
        self.dp = [[0] * (n+1) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                self.dp[i][j+1] = self.dp[i][j] + matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        _sum = 0
        for r in range(row1, row2 + 1):
            _sum += self.dp[r][col2 + 1] - self.dp[r][col1]
        return _sum

class TestCase(unittest.TestCase):
    def test_1(self):
        matrix = NumMatrix([[3, 0, 1, 4, 2],
                            [5, 6, 3, 2, 1], 
                            [1, 2, 0, 1, 5], 
                            [4, 1, 0, 1, 7], 
                            [1, 0, 3, 0, 5]])
        self.assertEqual(matrix.sumRegion(2, 1, 4, 3), 8)
        self.assertEqual(matrix.sumRegion(1, 1, 2, 2), 11)
        self.assertEqual(matrix.sumRegion(1, 2, 2, 4), 12)

if __name__ == '__main__':
    unittest.main()