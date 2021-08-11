"""
Reverse LinkedList in Place
"""
import unittest
from util_linkedlist import LinkedList as LinkedList

def reverse(head):
    if not head:
        return
    p, c, n = None, head, head.next
    while n:
        c.next = p
        p = c
        c = n
        n = n.next
    c.next = p
    return c

class TestCase(unittest.TestCase):
    def test_1(self):
        arr = [1, 2, 3]
        ll = LinkedList(arr)
        ll.head = reverse(ll.head)
        self.assertEqual(ll.print_list(), [3, 2, 1])

if __name__ == '__main__':
    unittest.main()