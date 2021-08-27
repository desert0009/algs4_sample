"""
168. Excel Sheet Column Title

Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 
Example 1:
Input: columnNumber = 1
Output: "A"

Example 2:
Input: columnNumber = 28
Output: "AB"

Example 3:
Input: columnNumber = 701
Output: "ZY"

Example 4:
Input: columnNumber = 2147483647
Output: "FXSHRXW"

Constraints:
1 <= columnNumber <= 231 - 1
"""
import unittest

def convert(n):
    ans = []
    while n > 0:
        r = n % 26
        n = n // 26
        if r == 0:
            r = 26
            n -= 1
        ans.append(chr(r + 64))
    return ''.join(ans[::-1])

class TestCase(unittest.TestCase):
    def test_1(self):
        n = 1
        self.assertEqual(convert(n), 'A')

    def test_2(self):
        n = 28
        self.assertEqual(convert(n), 'AB')
    
    def test_3(self):
        n = 701
        self.assertEqual(convert(n), 'ZY')
    
    def test_4(self):
        n = 2147483647
        self.assertEqual(convert(n), 'FXSHRXW')

if __name__ == '__main__':
    unittest.main()