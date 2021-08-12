"""
463. Island Perimeter (Easy)
"""
import unittest

def islandPerimeter(grid):
    m, n = len(grid), len(grid[0])
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    def dfs(i, j):
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] in [0, 2]:
            return 0
        _sum = cla_perimeter(i, j, m, n, grid)
        grid[i][j] = 2
        for dx, dy in dirs:
            _sum += dfs(i + dx, j + dy)
        return _sum

    def cla_perimeter(i, j, m, n, grid):
        _sum = 4
        if i > 0 and grid[i-1][j] in [1, 2]:
            _sum -= 1
        if i < m - 1 and grid[i+1][j] in [1, 2]:
            _sum -= 1
        if j > 0 and grid[i][j-1] in [1, 2]:
            _sum -= 1
        if j < n - 1 and grid[i][j + 1] in [1, 2]:
            _sum -= 1
        return _sum

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                return dfs(i, j)

class TestCase(unittest.TestCase):
    def test_1(self):
        grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
        self.assertEqual(islandPerimeter(grid), 16)

    def test_2(self):
        grid = [[1]]
        self.assertEqual(islandPerimeter(grid), 4)
    
    def test_3(self):
        grid = [[1,0]]
        self.assertEqual(islandPerimeter(grid), 4)

if __name__ == '__main__':
    unittest.main()