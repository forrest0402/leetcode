# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 22/6/2020 下午8:55
"""
from typing import List


class Node:

    def __init__(self, v: str):
        self.val = v
        self.nexts = dict()
        self.complete = False
        self.leaf = False

    def __setitem__(self, key, value):
        self.nexts[key] = value

    def __getitem__(self, item):
        return self.nexts[item]

    def __contains__(self, item):
        return item in self.nexts


class Solution:

    def dfs(self, text, idx, root, node: Node) -> bool:
        if idx == len(text):
            return node.complete

        if node.leaf:
            node = root

        if text[idx] in node and self.dfs(text, idx + 1, root, node[text[idx]]):
            return True

        if node.complete and self.dfs(text, idx, root, root):
            return True

        return False

    def wordBreak2(self, text: str, word_dict: List[str]) -> bool:
        dicts = Node('')
        for word in word_dict:
            cur = dicts
            for w in word:
                cur.leaf = False
                if w not in cur:
                    cur[w] = Node(w)
                cur = cur[w]
            cur.complete = True
            cur.leaf = True

        return self.dfs(text, 0, dicts, dicts)

    def wordBreak(self, text: str, word_dict: List[str]) -> bool:
        dp = [False for _ in range(len(text) + 1)]
        dp[0] = True
        dicts = dict()
        for word in word_dict:
            if len(word) not in dicts:
                dicts[len(word)] = set()
            dicts[len(word)].add(word)

        for i in range(1, len(text) + 1):
            for k, values in dicts.items():
                if i - k < 0:
                    continue
                sub = text[i - k:i]
                if sub in values:
                    dp[i] = dp[i] or dp[i - k]

        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.wordBreak(
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
        ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]))
