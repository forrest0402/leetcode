# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 26/2/2020 上午12:57
"""


class Solution:
    def pair(self, a, b):
        return (a == '(' and b == ')') or (a == '[' and b == ']') or (a == '{' and b == '}')

    def isValid(self, s: str) -> bool:
        if s is None or len(s) == 0:
            return True
        stack = []
        for c in s:
            if len(stack) == 0:
                stack.append(c)
                continue
            if self.pair(stack[-1], c):
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0
