# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 26/6/2020 下午3:55
"""

from typing import List


class Solution:

    def dfs(self, nums, idx, cur, target):

        if cur == target:
            return True

        if cur > target or idx >= len(nums):
            return False

        if nums[idx] > target:
            return False

        return self.dfs(nums, idx + 1, cur + nums[idx], target) or self.dfs(nums, idx + 1, cur, target)

    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False
        if max(nums) > s // 2:
            return False
        nums.sort(reverse=True)
        return self.dfs(nums, 0, 0, s // 2)
