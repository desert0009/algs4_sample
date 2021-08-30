"""
227. Basic Calculator II (Medium)

Given a string s which represents an expression, evaluate this expression and return its value. 
The integer division should truncate toward zero.
You may assume that the given expression is always valid. 
All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:
Input: s = "3+2*2"
Output: 7

Example 2:
Input: s = " 3/2 "
Output: 1

Example 3:
Input: s = " 3+5 / 2 "
Output: 5
 
Constraints:
1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
"""

'''
         "3  +   2   *      2"    +
stack [] [] [3] [3] [3,2]  [3,2] [3,4]
num   0  3   0   2   0      2     0
ope   +  +   +   +   *      *     +

Time: O(N), Space: O(N)
'''

import unittest

def calculator(s):
    stack, num, ope = [], 0, '+'
    for c in s + '+':
        if c.isdigit():
            num = (num * 10) + int(c)
        elif c in '+-/*':
            if ope == '+':
                stack.append(num)
            elif ope == '-':
                stack.append(num * -1)
            elif ope == '*':
                stack.append(stack.pop() * num)
            else:
                stack.append(int(stack.pop() / num))
            num, ope = 0, c
    return sum(stack)

class TestCase(unittest.TestCase):
    def test_1(self):
        s = "3+2*2"
        self.assertEqual(calculator(s), 7)
    
    def test_2(self):
        s = "14-3/2"
        self.assertEqual(calculator(s), 13)
    
    def test_3(self):
        s = " 3/2 "
        self.assertEqual(calculator(s), 1)
    
    def test_4(self):
        s = " 3+5 / 2 "
        self.assertEqual(calculator(s), 5)
    
    def test_5(self):
        s = " 32 / 2"
        self.assertEqual(calculator(s), 16)
    
    def test_6(self):
        s = "1-1+1"
        self.assertEqual(calculator(s), 1)

if __name__ == '__main__':
    unittest.main()
