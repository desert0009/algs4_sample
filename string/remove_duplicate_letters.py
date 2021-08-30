"""
316. Remove Duplicate Letters (Medium)

Given a string s, remove duplicate letters so that every letter appears once and only once. 
You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:
Input: s = "bcabc"
Output: "abc"

Example 2:
Input: s = "cbacdcbc"
Output: "acdb"
 
Constraints:
1 <= s.length <= 104
s consists of lowercase English letters.
"""

'''
                bcabc
c = b | stack = b
c = c | stack = bc
c = a | stack = a
c = b | stack = ab
c = c | stack = abc

Time: O(N), Space: O(N)
'''
import unittest

def remove(s):
    N = len(s)
    stack = []
    for i, c in enumerate(s):
        if c in stack:
            continue
        while stack and c <= stack[-1] and stack[-1] in s[i:]:
            stack.pop()
        stack.append(c)
    return ''.join(stack)

class TestCase(unittest.TestCase):
    def test_1(self):
        s = 'aaaa'
        self.assertEqual(remove(s), 'a')
    
    def test_2(self):
        s = 'bcabc'
        self.assertEqual(remove(s), 'abc')
    
    def test_3(self):
        s = 'cbacdcbc'
        self.assertEqual(remove(s), 'acdb')

if __name__ == '__main__':
    unittest.main()