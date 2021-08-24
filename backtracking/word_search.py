"""
79. Word Search (Medium)

Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
"""
import unittest

def exist(board, word):
    N = len(word)
    m, n = len(board), len(board[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    ans = False
    def dfs(i, j, idx):
        nonlocal ans
        if ans == True:
            return
        if i < 0 or j < 0 or i >= m or j >= n or idx == N or \
            board[i][j] == '-' or board[i][j] != word[idx]:
            return
        if idx == N - 1:
            ans = True
            return
        c = board[i][j]
        board[i][j] = '-'
        for dx, dy in dirs:
            dfs(i+dx, j+dy, idx+1)
        board[i][j] = c
    for i in range(m):
        for j in range(n):
            dfs(i, j, 0)
    return ans

class TestCase(unittest.TestCase):
    def test_1(self):
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        self.assertEqual(exist(board, 'ABCCED'), True)

    def test_2(self):
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        self.assertEqual(exist(board, 'SEE'), True)
    
    def test_3(self):
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        self.assertEqual(exist(board, 'ABCB'), False)

if __name__ == '__main__':
    unittest.main()