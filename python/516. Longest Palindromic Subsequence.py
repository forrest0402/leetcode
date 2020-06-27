# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 27/6/2020 下午9:06
"""


class Solution1:

    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for __ in range(n)] for _ in range(n)]

        for j in range(n):
            dp[j][j] = 1

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    if j - i == 1:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i + 1][j - 1] + 2

                else:
                    dp[i][j] = max(dp[i + 1][j - 1], dp[i + 1][j], dp[i][j - 1])

        return dp[0][-1]

    def valid(self, left, right, s):

        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True

    def longestPalindromeSubseq(self, s: str) -> int:

        n = len(s)
        dp = [[False for __ in range(n)] for _ in range(n)]
        ret = 0

        for j in range(n):
            dp[n - 1][j] = dp[j][n - 1] = self.valid(j, n - 1, s)
            dp[j][j] = True

        for i in range(n):
            dp[i][0] = dp[0][i] = self.valid(0, i, s)

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    if j - i == 1:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                    if dp[i][j]:
                        ret = max(ret, j - i + 1)
                else:
                    dp[i][j] = False

        return ret

