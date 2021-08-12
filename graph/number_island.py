import unittest

def dfs(matrix):
    m, n = len(matrix), len(matrix[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def _dfs(i, j, matrix):
        if i < 0 or j < 0 or i >= m or j >= n or matrix[i][j] == '0':
            return
        matrix[i][j] = '0'
        for dx, dy in dirs:
            _dfs(i + dx, j + dy, matrix)

    ans = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':
                ans += 1
                _dfs(i, j, matrix)
    return ans

class TestCase(unittest.TestCase):
    def test_1(self):
        grid = [["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]]
        self.assertEqual(dfs(grid), 1)
    
    def test_2(self):
        grid = [["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"]]
        self.assertEqual(dfs(grid), 3)

if __name__ == '__main__':
    unittest.main()