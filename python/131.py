# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 22/6/2020 下午6:26
"""


class Solution:

    def is_palindrome(self, text):
        if len(text) == 0:
            return False

        i = 0

        while i < len(text) // 2:
            if text[i] != text[-i - 1]:
                return False
            i += 1
        return True

    def dfs(self, s, idx, cur, ret):
        if idx == len(s):
            if self.is_palindrome(cur[-1]):
                ret.append(cur[:])
            return

        if len(cur) > 0 and self.is_palindrome(cur[-1]):
            self.dfs(s, idx + 1, cur + [s[idx]], ret)

        if len(cur) > 0:
            cur[-1] += s[idx]
        else:
            cur.append(s[idx])
        self.dfs(s, idx + 1, cur, ret)

    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 0:
            return [[]]
        ret = []
        self.dfs(s, 0, [], ret)
        return ret
