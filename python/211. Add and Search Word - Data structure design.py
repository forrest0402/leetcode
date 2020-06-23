# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 23/6/2020 下午6:02
"""


class WordDictionary:

    def __init__(self, v=None):
        """
        Initialize your data structure here.
        """
        self.dicts = dict()
        self.leaf = False
        self.val = v

    def addWord(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if not word:
            return

        node = self
        for w in word:
            if w not in node:
                node[w] = WordDictionary(w)
            node = node[w]

        node.leaf = True

    def _search(self, node, word, idx) -> bool:
        if idx >= len(word):
            return node.leaf

        if word[idx] in node:
            return self._search(node[word[idx]], word, idx + 1)

        if '.' == word[idx]:
            for k, v in node.dicts.items():
                if self._search(v, word, idx + 1):
                    return True

        return False

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if not word:
            return False

        return self._search(self, word, 0)

    def __contains__(self, item):
        return item in self.dicts

    def __setitem__(self, key, value):
        self.dicts[key] = value

    def __getitem__(self, item):
        return self.dicts[item]



if __name__ == "__main__":
    d = WordDictionary()
    d.addWord("a")
    d.addWord("ab")
    print(d.search("a"))
    print(d.search("a."))
    print(d.search("ab"))
    print(d.search(".a"))
    print(d.search(".b"))
    print(d.search("ab."))
    print(d.search("."))
    print(d.search(".."))
