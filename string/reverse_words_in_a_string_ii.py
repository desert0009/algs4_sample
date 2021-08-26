"""
Reverse Words in a String II

Given a character array s, reverse the order of the words.

A word is defined as a sequence of non-space characters. 
The words in s will be separated by a single space.

Your code must solve the problem in-place, i.e. without allocating extra space.

Example 1:
Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]

Example 2:
Input: s = ["a"]
Output: ["a"]
 

Constraints:
1 <= s.length <= 105
s[i] is an English letter (uppercase or lowercase), digit, or space ' '.
There is at least one word in s.
s does not contain leading or trailing spaces.
All the words in s are guaranteed to be separated by a single space.
"""
import unittest

def reverseWords(s):
    def reverse(s, l, r):
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

    reverse(s, 0, len(s) - 1)
    l = 0
    for i in range(len(s)):
        if s[i] == ' ':
            reverse(s, l, i-1)
            l = i + 1
    reverse(s, l, len(s)-1)

class TestCase(unittest.TestCase):
    def test_1(self):
        s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
        reverseWords(s)
        self.assertEqual(s, ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"])
    
    def test_2(self):
        s = ["a"]
        reverseWords(s)
        self.assertEqual(s, ["a"])

if __name__ == '__main__':
    unittest.main()
