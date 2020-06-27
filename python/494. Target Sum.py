# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 27/6/2020 下午5:52
"""


class Solution:

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        max_sum = sum(nums)
        if max_sum < S:
            return 0

        dp = [[0 for __ in range(2 * max_sum + 1)] for _ in range(len(nums))]
        if nums[0] == 0:
            dp[0][nums[0] + max_sum] = dp[0][-nums[0] + max_sum] = 2
        else:
            dp[0][nums[0] + max_sum] = dp[0][-nums[0] + max_sum] = 1
        for i in range(1, len(nums)):
            for s in range(2 * max_sum + 1):
                if s - nums[i] >= 0:
                    dp[i][s] += dp[i - 1][s - nums[i]]
                if s + nums[i] <= 2 * max_sum:
                    dp[i][s] += dp[i - 1][s + nums[i]]

        return dp[-1][S + max_sum]
