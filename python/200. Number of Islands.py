# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 23/6/2020 下午2:52
"""

from typing import List


class Solution:
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        ret = 0
        q = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                q.append((i, j))
                while q:
                    x, y = q.pop(0)

                    if grid[x][y] == '0':
                        continue

                    grid[x][y] = '0'

                    for di, dj in self.directions:
                        nx, ny = x + di, y + dj
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                            q.append((nx, ny))

                ret += 1

        return ret
