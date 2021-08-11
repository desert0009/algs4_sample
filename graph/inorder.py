"""
Given root of binary tree. Use DFS to get the inorder traversal of its node's values
"""

import unittest
import util_binary_tree as binary_tree

def inorder(root):
    path = []
    def _inorder(root):
        if not root:
            return
        _inorder(root.left)
        path.append(str(root.val))
        _inorder(root.right)
    _inorder(root)
    return path

class TestCase(unittest.TestCase):
    def test_1(self):
        arr = ['2', '1', '3', '-', '-', '-', '-']
        root = binary_tree.BinaryTree(arr).root
        self.assertEqual(inorder(root), ['1', '2', '3'])

if __name__ == '__main__':
    unittest.main()