"""
547. Number of Provinces (Medium)

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Example 1:
    1 -- 2
       3
    Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    Output: 2

Example 2:
    1   2
      3
    Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    Output: 3
"""

# Union Find

import unittest

class TestCase(unittest.TestCase):
    def test_1(self):
        isConnected = [[1,1,0],[1,1,0],[0,0,1]]
        self.assertEqual(findCircleNum(isConnected), 2)
    
    def test_2(self):
        isConnected = [[1,0,0],[0,1,0],[0,0,1]]
        self.assertEqual(findCircleNum(isConnected), 3)

def findCircleNum(isConnected):
    N = len(isConnected)
    ids = [i for i in range(N)]
    
    def union(i, j):
        root_i, root_j = find(i), find(j)
        ids[root_i] = root_j
    
    # find the root
    def find(i):
        if i != ids[i]:
            i = ids[i]
        return i
    
    for i in range(N):
        for j in range(N):
            if i != j and isConnected[i][j] == 1:
                union(i, j)
    
    roots = set()
    for _id in ids:
        root_id = find(_id)
        roots.add(root_id)
    return len(roots)

if __name__ == '__main__':
    unittest.main()
    print('PASS!')

