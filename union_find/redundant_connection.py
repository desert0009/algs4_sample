"""
684. Redundant Connection (Medium)

In this problem, a tree is an undirected graph that is connected and has no cycles.
You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.
Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

Example 1:
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

Example 2:
Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]

Constraints:
n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
"""

"""
Idea:
Let [p, q] = edges. Union Find to find the p's root and q's root
if p's root == q's root, then [p, q] is redundant connection
"""

import unittest

class UnionFind:
    def __init__(self, n):
        self.ids = [i for i in range(n + 1)]

    def union(self, p, q):
        root_p, root_q = self.find(p), self.find(q)
        if root_p == root_q:
            return True
        self.ids[root_p] = self.ids[root_q]
        return False
    
    def find(self, p):
        while p != self.ids[p]:
            p = self.ids[p]
        return p

def findRedundantConnection(edges):
    n = len(edges)
    union_find = UnionFind(n)
    for p, q in edges:
        is_redundant = union_find.union(p, q)
        if is_redundant:
            return [p, q]

class TestCase(unittest.TestCase):
    def test_1(self):
        edges = [[1,2],[1,3],[2,3]]
        self.assertEqual(findRedundantConnection(edges), [2, 3])
    
    def test_2(self):
        edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
        self.assertEqual(findRedundantConnection(edges), [1, 4])

if __name__ == '__main__':
    unittest.main()