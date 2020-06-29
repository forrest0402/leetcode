# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 30/6/2020 上午12:31
"""

from typing import List


class Solution:

    def find(self, union, x):
        if union[x] == x:
            return x;
        else:
            return self.find(union, union[x])

    def merge(self, union, i, j, ret):
        head_i = self.find(union, i)
        head_j = self.find(union, j)
        union[head_i] = head_j
        if head_i in ret:
            ret.remove(head_i)
        ret.add(head_j)

    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        union = [i for i in range(n)]
        ret = set(union)

        for i in range(n):
            for j in range(i + 1, n):
                if M[i][j] == 0:
                    continue

                self.merge(union, i, j, ret)

        # print(ret)
        return len(ret)
