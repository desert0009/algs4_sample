"""
1026. Maximum Difference Between Node and Ancestor

Given the root of a binary tree, find the maximum value v for 
which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.
"""

import unittest
from util_binary_tree import BinaryTree

def max_diff(root):
    if not root:
        return 0
    ans = 0
    def dfs(root, _max, _min):
        if not root:
            return
        nonlocal ans
        _max = max(_max, root.val)
        _min = min(_min, root.val)
        ans = max(ans, abs(root.val - _max), abs(root.val - _min))
        dfs(root.left, _max, _min)
        dfs(root.right, _max, _min)
    dfs(root, root.val, root.val)
    return ans

class TestCase(unittest.TestCase):
    def test_1(self):
        arr = [8, 3, 10, 1, 6, 14, '-', '-', 4, 7, 3, '-', '-', '-', '-', '-', '-', '-', '-']
        root = BinaryTree(arr).root
        self.assertEqual(max_diff(root), 7)
    
    def test_2(self):
        arr = [1, '-', 2, '-', 0, 3, '-', '-', '-']
        root = BinaryTree(arr).root
        self.assertEqual(max_diff(root), 3)

if __name__ == '__main__':
    unittest.main()