"""
208. Implement Trie (Prefix Tree) (Medium)

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
"""

import unittest

class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word):
        cur = self.trie
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['$'] = word
        print(self.trie)

    def search(self, word):
        cur = self.trie
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        return '$' in cur

    def startsWith(self, word):
        cur = self.trie
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        return True

class TestCase(unittest.TestCase):
    def test_1(self):
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.search("apple"))
        self.assertFalse(trie.search("app"))
        self.assertTrue(trie.startsWith("app"))
        trie.insert("app")
        self.assertTrue(trie.search("app"))

if __name__ == '__main__':
    unittest.main()


