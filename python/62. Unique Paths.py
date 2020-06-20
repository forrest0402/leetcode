# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 20/6/2020 下午6:39
"""


class Solution:
    def dfs(self, i, j, m, n):
        if i == m and j == n:
            return 1

        if i > m or j > n:
            return 0

        return self.dfs(i + 1, j, m, n) + self.dfs(i, j + 1, m, n)

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for __ in range(m)]

        for i in range(m):
            dp[i][0] = 1

        for i in range(n):
            dp[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]


if __name__ == "__main__":
    s = Solution()
    print(s.uniquePaths(1, 1))
