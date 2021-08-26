"""
Reverse Words in a String

Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. 
The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. 
The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

Example 4:
Input: s = "  Bob    Loves  Alice   "
Output: "Alice Loves Bob"

Example 5:
Input: s = "Alice does not even like bob"
Output: "bob like even not does Alice"
 

Constraints:
1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.
 

Follow-up: If the string data type is mutable in your language, 
can you solve it in-place with O(1) extra space?
"""
import unittest

def reverseWords(s):
    # Time: O(N), Space: O(N)
    _list = s.split(' ')
    _list = [s for s in _list if s]
    l, r = 0, len(_list) - 1
    while l < r:
        _list[l], _list[r] = _list[r], _list[l]
        l += 1
        r -= 1
    return ' '.join(_list)

class TestCase(unittest.TestCase):
    def test_1(self):
        s = "the sky is blue"
        self.assertEqual(reverseWords(s), "blue is sky the")

    def test_2(self):
        s = "  Bob    Loves  Alice   "
        self.assertEqual(reverseWords(s), "Alice Loves Bob")
    
    def test_3(self):
        s = "  hello world  "
        self.assertEqual(reverseWords(s), "world hello")


if __name__ == '__main__':
    unittest.main()
