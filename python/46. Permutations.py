# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 14/6/2020 下午6:48
"""
from typing import List


class Solution:

    def dfs(self, nums: List[int], idx: int) -> List[List[int]]:
        if len(nums) <= idx + 1:
            return [[nums[idx]]]

        f = nums[idx]
        res = []
        for p in self.dfs(nums, idx + 1):
            for i in range(1, len(p)):
                res.append(p[:i] + [f] + p[i:])
            res.append([f] + p)
            res.append(p + [f])

        return res

    def permute(self, nums: List[int]) -> List[List[int]]:
        if nums is None or len(nums) == 0:
            return [[]]

        if len(nums) == 1:
            return [nums]

        return self.dfs(nums, 0)


if __name__ == "__main__":
    s = Solution()
    print(s.permute([1]))
