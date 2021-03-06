# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 11/7/2020 下午9:35
"""

import numpy as np


class Solution:
    def knightDialer2(self, N: int) -> int:

        dp = [[0 for _ in range(N)] for __ in range(10)]
        for i in range(10):
            dp[i][0] = 1

        for i in range(1, N):
            dp[0][i] = dp[4][i - 1] + dp[6][i - 1]
            dp[1][i] = dp[6][i - 1] + dp[8][i - 1]
            dp[2][i] = dp[7][i - 1] + dp[9][i - 1]
            dp[3][i] = dp[4][i - 1] + dp[8][i - 1]
            dp[4][i] = dp[9][i - 1] + dp[3][i - 1] + dp[0][i - 1]
            # dp[5][i] = dp[4][i-1]+dp[6][i-1]
            dp[6][i] = dp[1][i - 1] + dp[7][i - 1] + dp[0][i - 1]
            dp[7][i] = dp[2][i - 1] + dp[6][i - 1]
            dp[8][i] = dp[1][i - 1] + dp[3][i - 1]
            dp[9][i] = dp[4][i - 1] + dp[2][i - 1]

        return (dp[0][-1] + dp[1][-1] + dp[2][-1] + dp[3][-1] + dp[4][-1] + dp[5][-1] + dp[6][-1] + dp[7][-1] + dp[8][
            -1] + dp[9][-1]) % (10 ** 9 + 7)

    def knightDialer(self, N):
        if N == 1:
            return 10

        mod = 10 ** 9 + 7
        M = np.array([[0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                      [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                      [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                      [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                      [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                      [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                      [0, 0, 1, 0, 1, 0, 0, 0, 0, 0]])
        res, N = np.ones(10), N - 1
        while N:
            if N % 2:
                res = np.matmul(res, M) % mod
            M = (M @ M) % mod
            N //= 2
        return int(np.sum(res)) % mod


if __name__ == "__main__":
    s = Solution()
    print(s.knightDialer(20))
