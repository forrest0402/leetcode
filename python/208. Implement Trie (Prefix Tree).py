# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 23/6/2020 下午4:17
"""


class Trie:

    def __init__(self, v=None):
        """
        Initialize your data structure here.
        """
        self.dicts = dict()
        self.leaf = False
        self.val = v

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if not word:
            return

        node = self.dicts
        for w in word:
            if w not in node:
                node[w] = Trie(w)
            node = node[w]

        node.leaf = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if not word:
            return False

        node = self.dicts
        for w in word:
            if w not in node:
                return False

            node = node[w]

        return node.leaf

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if not word:
            return False

        node = self.dicts
        for w in word:
            if w not in node:
                return False

            node = node[w]

        return True

    def __contains__(self, item):
        return item in self.dicts

    def __setitem__(self, key, value):
        self.dicts[key] = value

    def __getitem__(self, item):
        return self.dicts[item]


if __name__ == "__main__":
    word = 'apple'
    obj = Trie()
    obj.insert(word)
    print(obj.search('app'))
    print(obj.search('app'))
    print(obj.startsWith('app'))
