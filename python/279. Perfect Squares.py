# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 24/6/2020 下午4:11
"""
import math


class Solution:

    def numSquares(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        f = math.floor(math.sqrt(n))
        dp = [2 ** 31 for _ in range(n + 1)]
        i = 1
        while i * i <= n:
            dp[i * i] = 1
            i += 1

        for i in range(n + 1):
            if dp[i] != 2 ** 31:
                continue

            j = 1
            while j * j < i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1

        return dp[n]
