"""
695. Max Area of Island (Medium)
"""
import unittest

def maxAreaOfIsland(grid):
    m, n = len(grid), len(grid[0])
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    def _dfs(grid, i, j):
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
            return 0
        grid[i][j] = 0
        _sum = 1
        for dx, dy in dirs:
            _sum += _dfs(grid, i + dx, j + dy)
        return _sum

    ans = 0
    for i in range(m):
        for j in range(n):
            ans = max(ans, _dfs(grid, i, j))
    return ans

class TestCase(unittest.TestCase):
    def test_1(self):
        grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,1,1,0,1,0,0,0,0,0,0,0,0],
                [0,1,0,0,1,1,0,0,1,0,1,0,0],
                [0,1,0,0,1,1,0,0,1,1,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,0,0,0,0,0,0,1,1,0,0,0,0]]
        self.assertEqual(maxAreaOfIsland(grid), 6)
    
    def test_2(self):
        grid = [[0,0,0,0,0,0,0,0]]
        self.assertEqual(maxAreaOfIsland(grid), 0)

if __name__ == '__main__':
    unittest.main()