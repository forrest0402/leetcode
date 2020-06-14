# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 14/6/2020 下午11:20
"""

import math
from typing import List


class Solution:

    def axis(self, x, y, n):
        nx = y
        ny = n - x - 1
        return nx, ny

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        if matrix is None or len(matrix) == 0:
            return

        n = len(matrix)
        circle_n = math.ceil(n / 2)

        for row in range(circle_n):
            for col in range(row, n - row - 1):
                ox, oy = row, col
                nx, ny = self.axis(ox, oy, n)
                oldn = matrix[ox][oy]
                while (row, col) != (nx, ny):
                    newn = matrix[nx][ny]
                    matrix[nx][ny] = oldn
                    oldn = newn
                    nx, ny = self.axis(nx, ny, n)
                matrix[nx][ny] = oldn


if __name__ == "__main__":
    s = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s.rotate(matrix)
    print(matrix)
