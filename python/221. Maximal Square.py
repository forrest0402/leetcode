# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 23/6/2020 下午7:29
"""

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])

        ret = 0
        dp = [[0 for __ in range(n)] for _ in range(m)]

        # dp[:][0] = map(int, matrix[:][0])
        # dp[0][:] = map(int, matrix[0][:])

        for i in range(m):
            if matrix[i][0] == '1':
                dp[i][0] = 1
                ret = 1

        for i in range(n):
            if matrix[0][i] == '1':
                dp[0][i] = 1
                ret = 1

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    ret = max(ret, dp[i][j])

        return ret * ret


if __name__ == "__main__":
    s = Solution()
    print(s.maximalSquare([["0", "1"], ["1", "0"]]))
