"""
5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Example 3:
Input: s = "a"
Output: "a"

Example 4:
Input: s = "ac"
Output: "a"

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""
import unittest

def longest(s):
    N = len(s)
    ans = ''
    max_len = 0

    for i in range(N):
        if i + max_len >= N:
            break
        for j in range(i + max_len, N):
            _s = s[i:j+1]
            if _s == _s[::-1]:
                max_len = j - i + 1
                ans = _s
    return ans

class TestCase(unittest.TestCase):
    def test_1(self):
        s = 'a'
        self.assertEqual(longest(s), 'a')

    def test_2(self):
        s = 'babad'
        self.assertEqual(longest(s), 'bab')
    
    def test_3(self):
        s = 'cbbd'
        self.assertEqual(longest(s), 'bb')

if __name__ == '__main__':
    unittest.main()