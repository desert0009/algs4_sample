"""
Stack Application Example

Evaluate standard input, and check the output number.
"""

import unittest

def evaluation(exp):
    val_stack, ope_stack = [], []
    for c in exp.split(' '):
        if c in ['+', '-', '/', '*', 'sqrt']:
            ope_stack.append(c)
        elif c == '(':
            pass
        elif c == ')':
            op = ope_stack.pop()
            v1 = val_stack.pop()
            if op == '+':      v1 = val_stack.pop() + v1
            elif op == '-':    v1 = val_stack.pop() - v1
            elif op == '*':    v1 = val_stack.pop() * v1
            elif op == '/':    v1 = val_stack.pop() / v1
            elif op == 'sqrt': v1 = v1 ** 0.5
            val_stack.append(v1)
        else:
            val_stack.append(float(c))
    return round(val_stack.pop(), 2)

class TestClass(unittest.TestCase):    
    def test_expression_1(self):
        exp = '( 1 + ( ( 2 + 3 ) * ( 4 * 5 ) ) )'
        self.assertEqual(evaluation(exp), 101.00)

    def test_expression_2(self):
        exp = '( ( 1 + sqrt ( 5.0 ) ) * 0.5 )'
        self.assertEqual(evaluation(exp), 1.62)
    
    def test_expression_3(self):
        exp = '( 9 / 6 )'
        self.assertEqual(evaluation(exp), 1.5)

if __name__ == '__main__':
    unittest.main()