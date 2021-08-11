"""
Linked List Utility
"""

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self, arr):
        self.head = self.build(arr)

    def build(self, arr):
        dummy_head = Node(0)
        cur = dummy_head
        for a in arr:
            node = Node(a)
            cur.next = node
            cur = cur.next
        return dummy_head.next

    def print_list(self):
        l = []
        cur = self.head
        while cur:
            l.append(cur.val)
            cur = cur.next
        print(l)
        return l

def __run_tests():
    arr = [1, 2, 3]
    ll = LinkedList(arr)
    ll.print_list()

if __name__ == '__main__':
    __run_tests()