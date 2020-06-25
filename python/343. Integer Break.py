# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 25/6/2020 下午4:57
"""
import math


class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        for i in range(2, n + 1):
            limit = math.ceil(i / 2) + 1
            for j in range(1, limit):
                n1 = max(dp[i - j], i - j)
                n2 = max(dp[j], j)
                dp[i] = max(n1 * n2, dp[i])

        # print(dp)
        return dp[n]


if __name__ == "__main__":
    s = Solution()
    print(s.integerBreak(10))
