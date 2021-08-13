import unittest
from util_binary_tree import BinaryTree as BinaryTree

def is_valid_bst(root):
    pre_node = None
    def _is_valid(root):
        nonlocal pre_node
        if not root:
            return True
        left = _is_valid(root.left)
        if pre_node and int(pre_node.val) >= int(root.val):
            return False
        pre_node = root
        right = _is_valid(root.right)
        return left and right
    return _is_valid(root)

class TestCase(unittest.TestCase):
    def test_1(self):
        arr = ['2', '1', '3', '-', '-', '-', '-']
        root = BinaryTree(arr).root
        self.assertTrue(is_valid_bst(root))
    
    def test_2(self):
        arr = ['1', '2', '3', '-', '-', '-', '-']
        root = BinaryTree(arr).root
        self.assertFalse(is_valid_bst(root))
    
    def test_3(self):
        arr = []
        root = BinaryTree(arr).root
        self.assertTrue(is_valid_bst(root))

if __name__ == '__main__':
    unittest.main()
