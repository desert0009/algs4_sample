"""
Given root of binary tree. Use BFS to get the level order traversal of its node's values
"""

import unittest
import util_binary_tree as binary_tree

def level_order(root):
    if not root:
        return []
    q = [root]
    ans = []
    while q:
        ans.append([])
        for _ in range(len(q)):
            v = q.pop(0)
            ans[-1].append(int(v.val))
            if v.left:
                q.append(v.left)
            if v.right:
                q.append(v.right)
    return ans

class TestClass(unittest.TestCase):    
    def test_levelorder_1(self):
        arr = ['1', '2', '3', '-', '-', '4', '5', '-', '-', '-', '-']
        root = binary_tree.BinaryTree(arr).root
        self.assertEqual(level_order(root), [[1], [2, 3], [4, 5]])

    def test_levelorder_2(self):
        arr = ['1', '-', '-']
        root = binary_tree.BinaryTree(arr).root
        self.assertEqual(level_order(root), [[1]])
    
    def test_levelorder_3(self):
        arr = []
        root = binary_tree.BinaryTree(arr).root
        self.assertEqual(level_order(root), [])

if __name__ == '__main__':
    unittest.main()