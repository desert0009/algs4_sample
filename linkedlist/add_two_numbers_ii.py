"""
Add Two Numbers II

You are given two non-empty linked lists representing two non-negative integers. 
The most significant digit comes first and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]

Example 2:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]

Example 3:
Input: l1 = [0], l2 = [0]
Output: [0]
"""

import unittest

class Node():
    def __init__(self, x):
        self.val = x
        self.next = None

def build_linked_list(nums):
    if not nums:
        return None
    dummy_h = Node(0)
    cur = dummy_h
    for n in nums:
        node = Node(n)
        cur.next = node
        cur = cur.next
    return dummy_h.next # head

def get_linked_list_vals(head):
    if not head:
        return []
    nodes = []
    cur = head
    while cur:
        nodes.append(cur.val)
        cur = cur.next
    return nodes

def reverse_linked_list(head):
    if not head:
        return None
    p, c, n = None, head, head.next
    while n:
        c.next = p
        p = c
        c = n
        n = n.next
    c.next = p
    return c 

def add(l1, l2):
    dummy_h = Node(0)
    cur = dummy_h
    prefix = 0
    l1 = reverse_linked_list(l1)
    l2 = reverse_linked_list(l2)
    while l1 or l2:
        _sum = prefix
        if l1:
            _sum += l1.val
            l1 = l1.next
        if l2:
            _sum += l2.val
            l2 = l2.next
        node = Node(_sum % 10)
        prefix = _sum // 10
        cur.next = node
        cur = cur.next
    
    if prefix:
        node = Node(prefix)
        cur.next = node
        cur = cur.next

    head = reverse_linked_list(dummy_h.next)
    return head

class TestCase(unittest.TestCase):
    def test_1(self):
        l1 = build_linked_list([2, 4, 3])
        l2 = build_linked_list([5, 6, 4])
        head = add(l1, l2)
        nodes = get_linked_list_vals(head)
        self.assertEqual(nodes, [8, 0, 7])
    
    def test_2(self):
        l1 = build_linked_list([7, 2, 4, 3])
        l2 = build_linked_list([5, 6, 4])
        head = add(l1, l2)
        nodes = get_linked_list_vals(head)
        self.assertEqual(nodes, [7, 8, 0, 7])
    
    def test_3(self):
        l1 = build_linked_list([5])
        l2 = build_linked_list([5])
        head = add(l1, l2)
        nodes = get_linked_list_vals(head)
        self.assertEqual(nodes, [1, 0])


if __name__ == '__main__':
    unittest.main()