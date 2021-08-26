"""
Valid Palindrome

Given a string s, determine if it is a palindrome, 
considering only alphanumeric characters and ignoring cases.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
 
Constraints:
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""
import unittest

def isPalindrome(s):
    l, r = 0, len(s) - 1
    while l < r:
        if not s[l].isalnum():
            l += 1
            continue
        if not s[r].isalnum():
            r -= 1
            continue
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True

class TestCase(unittest.TestCase):
    def test_1(self):
        s = "A man, a plan, a canal: Panama"
        self.assertTrue(isPalindrome(s))
    
    def test_2(self):
        s = "race a car"
        self.assertFalse(isPalindrome(s))
    
    def test_3(self):
        s = ""
        self.assertTrue(isPalindrome(s))
    
    def test_4(self):
        s = " "
        self.assertTrue(isPalindrome(s))
    
    def test_5(self):
        s = "09"
        self.assertFalse(isPalindrome(s))
    
    def test_6(self):
        s = "0 e9"
        self.assertFalse(isPalindrome(s))
    
    def test_7(self):
        s = "0P"
        self.assertFalse(isPalindrome(s))

if __name__ == '__main__':
    unittest.main()