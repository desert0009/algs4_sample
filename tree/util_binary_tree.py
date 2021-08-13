"""
Binary Tree Utility
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, arr):
        self.root = self.decode(arr)

    def encode(self):
        if not self.root:
            return []
        queue = [self.root]
        res = []
        while queue:
            for _ in range(len(queue)):
                v = queue.pop(0)
                res.append(str(v.val) if v else '-')
                if v:
                    queue.append(v.left)
                    queue.append(v.right)
        return res

    def decode(self, arr):
        if not arr:
            return None
        root = TreeNode(arr.pop(0))
        queue = [root]
        while queue:
            for _ in range(len(queue)):
                v = queue.pop(0)
                l, r = arr.pop(0), arr.pop(0)
                if l != '-':
                    node = TreeNode(int(l))
                    queue.append(node)
                    v.left = node
                if r != '-':
                    node = TreeNode(int(r))
                    queue.append(node)
                    v.right = node
        return root

def __test_case():
    inp_arr = ['1', '2', '3', '-', '-', '4', '5', '-', '-', '-', '-']
    root = BinaryTree(inp_arr[:])
    assert root.encode() == inp_arr

if __name__ == '__main__':
    __test_case()