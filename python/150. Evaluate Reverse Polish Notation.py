# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 22/6/2020 下午11:27
"""
from typing import List


class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ret = 0
        for token in tokens:
            if token == '+':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n1 + n2)
            elif token == '-':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2 - n1)
            elif token == '*':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n1 * n2)
            elif token == '/':
                n1 = stack.pop()
                n2 = stack.pop()
                flag = True if n1 * n2 < 0 else False
                stack.append(-(-n2 // n1) if flag else n2 // n1)
            else:
                stack.append(int(token))

        return stack.pop()


if __name__ == "__main__":
    s = Solution()
    print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
