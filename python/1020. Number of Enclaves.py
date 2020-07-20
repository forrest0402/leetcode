# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 20/7/2020 下午11:14
"""

import json
from typing import List


class Solution:
    dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def numEnclaves(self, A: List[List[int]]) -> int:

        if not A or not A[0]:
            return 0

        m = len(A)
        n = len(A[0])

        def mark(A, i, j):
            q = []
            if A[i][j] == 1:
                q.append((i, j))
            A[i][j] = 0
            while len(q) > 0:
                x, y = q.pop(0)
                for dx, dy in self.dir:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= m or ny < 0 or ny >= n:
                        continue
                    if A[nx][ny] == 1:
                        A[nx][ny] = 0
                        q.append((nx, ny))

        for i in range(m):
            if A[i][0] == 1:
                mark(A, i, 0)
            if A[i][n - 1] == 1:
                mark(A, i, n - 1)

        for j in range(1, n - 1):
            if A[0][j] == 1:
                mark(A, 0, j)
            if A[m - 1][j] == 1:
                mark(A, m - 1, j)

        ret = 0
        for x in A:
            ret += sum(x)

        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.numEnclaves([[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))
    print(s.numEnclaves([[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]))
    print(s.numEnclaves([[]]))
