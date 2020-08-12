# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 12/8/2020 下午8:39
"""

from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # g = [[0 for __ in range(n)] for _ in range(n)]
        sp = [[2 ** 31 if i != j else 0 for j in range(n)] for i in range(n)]
        for e in edges:
            sp[e[0]][e[1]] = sp[e[1]][e[0]] = e[2]

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    sp[i][j] = min(sp[i][j], sp[i][k] + sp[k][j])

        ret, min_n = 0, 2 ** 31
        for i in range(n):
            num = len(list(filter(lambda x: 0 < x <= distanceThreshold, sp[i])))
            # print(sp[i], num)
            if num <= min_n:
                min_n = num
                ret = i

        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.findTheCity(5, [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], 2))
