"""
93. Restore IP Addresses (Medium)

Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s. You can return them in any order.
A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single dots and cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses. 

Example 1:
Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]

Example 2:
Input: s = "0000"
Output: ["0.0.0.0"]

Example 3:
Input: s = "1111"
Output: ["1.1.1.1"]

Example 4:
Input: s = "010010"
Output: ["0.10.0.10","0.100.1.0"]

Example 5:
Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 
Constraints:
0 <= s.length <= 3000
s consists of digits only.
"""
import unittest

def restore(s):
    N = len(s)
    if N < 0 or N > 12:
        return []
    
    ans = []
    def dfs(i, path):
        if i > N:
            return
        elif i == N and len(path) == 4:
            ans.append('.'.join(path[:]))
            return
        elif len(path) == 4: # and i < N
            return
        
        for j in range(3):
            if i + j >= N:
                break
            _str = s[i: i+j+1]
            num = int(_str)
            if str(num) == _str and 0 <= num <= 255:
                path.append(_str)
                dfs(i+j+1, path)
                path.pop()
    dfs(0, [])
    return ans

class TestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(restore('25525511135'), ["255.255.11.135","255.255.111.35"])
    
    def test_2(self):
        self.assertEqual(restore('0000'), ["0.0.0.0"])
    
    def test_3(self):
        self.assertEqual(restore('1111'), ["1.1.1.1"])
    
    def test_4(self):
        self.assertEqual(restore('101023'), ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"])

if __name__ == '__main__':
    unittest.main()