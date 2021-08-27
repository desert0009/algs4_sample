"""
Excel Sheet Column Number

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
Input: "A"
Output: 1


Example 2:
Input: "AB"
Output: 28

Example 3:
Input: "ZY"
Output: 701

Example 4:
Input: "FXSHRXW"
Output: 2147483647

Constraints:
1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].
"""
import unittest

def convert(columnTitle):
    columnTitle = list(columnTitle)[::-1]
    _sum = 0
    for i in range(len(columnTitle)):
        c = columnTitle[i]
        _sum += (26 ** i) * (ord(c) - 64)
    return _sum

class TestCase(unittest.TestCase):
    def test_0(self):
        columnTitle = 'A'
        self.assertEqual(convert(columnTitle), 1)

    def test_1(self):
        columnTitle = 'AB'
        self.assertEqual(convert(columnTitle), 28)
    
    def test_2(self):
        columnTitle = 'ZY'
        self.assertEqual(convert(columnTitle), 701)
    
    def test_3(self):
        columnTitle = 'FXSHRXW'
        self.assertEqual(convert(columnTitle), 2147483647)

if __name__ == '__main__':
    unittest.main()