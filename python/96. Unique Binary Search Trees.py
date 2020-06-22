# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 22/6/2020 下午12:02
"""


class Solution:
    def divide_and_conquer(self, s, e):
        if s >= e:
            return 1

        ret = 0
        for mid in range(s, e + 1):
            lefts = self.divide_and_conquer(s, mid - 1)
            rights = self.divide_and_conquer(mid + 1, e)
            ret += lefts * rights
        return ret

    def numTrees2(self, n: int) -> int:
        return self.divide_and_conquer(1, n)

    def numTrees(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[0] = dp[1] = 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]

        return dp[n]


if __name__ == "__main__":
    s = Solution()
    for i in range(1, 10):
        print(s.numTrees(i), s.numTrees2(i))
