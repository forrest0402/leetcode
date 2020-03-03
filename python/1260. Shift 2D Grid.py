# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 2/3/2020 下午9:48
"""
from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ni = (i + k // n + (1 if k % n + j >= n else 0)) % m
                nj = (j + k % n) % n
                res[ni][nj] = grid[i][j]

        return res


if __name__ == "__main__":
    s = Solution()
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 1
    print(s.shiftGrid(grid, k))
