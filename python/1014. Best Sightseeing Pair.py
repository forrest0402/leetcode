# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 18/7/2020 下午10:11
"""

from typing import List


class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        dp = [0 for _ in range(len(A))]
        dp[1] = A[1] + A[0] - 1
        ret = dp[1]
        for i in range(2, len(A)):
            dp[i] = max(dp[i - 1] - 1 + A[i] - A[i - 1], A[i] + A[i - 1] - 1)
            ret = max(dp[i], ret)

        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.maxScoreSightseeingPair([8, 5, 6, 7, 9]))
    print(s.maxScoreSightseeingPair([2, 2, 2]))  # 3
    print(s.maxScoreSightseeingPair([8, 1, 5, 2, 6]))
