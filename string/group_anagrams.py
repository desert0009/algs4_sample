"""
Group Anagrams
"""
import unittest
import collections

def group_anagrams(strs):
    dic = {}
    for s in strs:
        key = ''.join(sorted(s))
        dic[key] = dic.get(key, [])
        dic[key].append(s)
    ans = []
    for key in dic:
        ans.append(dic[key])
    return ans

class TestCase(unittest.TestCase):
    def test_1(self):
        strs = ["eat","tea","tan","ate","nat","bat"]
        gt = [["bat"],["nat","tan"],["ate","eat","tea"]]
        dt = group_anagrams(strs)
        self.assertEqual(gt.sort(), dt.sort())

    def test_2(self):
        strs = [""]
        gt = [[""]]
        dt = group_anagrams(strs)
        self.assertEqual(gt.sort(), dt.sort())

    def test_3(self):
        strs = ["a"]
        gt = [["a"]]
        dt = group_anagrams(strs)
        self.assertEqual(gt.sort(), dt.sort())

if __name__ == '__main__':
    unittest.main()