"""
212. Word Search II (Hard)

Given an m x n board of characters and a list of strings words, return all words on the board.
Each word must be constructed from letters of sequentially adjacent cells, 
where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once in a word.

Example 1:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], 
       words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:
Input: board = [["a","b"],["c","d"]],
       words = ["abcb"]
Output: []
"""
import unittest

class Trie():
    def __init__(self, words):
        self.trie = {}
        for word in words:
            self.build_trie(word)

    def build_trie(self, word):
        cur = self.trie
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['$'] = word

def findWords(board, words):
    trie = Trie(words).trie
    dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    m, n = len(board), len(board[0])

    ans = set()
    def dfs(i, j, path, cur):
        if i < 0 or j < 0 or i >= m or j >= n or board[i][j] == '-':
            return
        
        c = board[i][j]
        if c not in cur:
            return
        board[i][j] = '-'
        cur = cur[c]
        path.append(c)
        if '$' in cur:
            ans.add(''.join(path[:]))
        for dx, dy in dirs:
            dfs(i+dx, j+dy, path, cur)

        path.pop()
        board[i][j] = c
        
    for i in range(m):
        for j in range(n):
            if board[i][j] in trie:
                dfs(i, j, [], trie)
    return list(ans)

class TestCase(unittest.TestCase):
    def test_1(self):
        board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
        words = ["oath","pea","eat","rain"]
        self.assertEqual(findWords(board, words), ['eat', 'oath'])
    
    def test_2(self):
        board = [["a","b"],["c","d"]]
        words = ["abcb"]
        self.assertEqual(findWords(board, words), [])

if __name__ == '__main__':
    unittest.main()
