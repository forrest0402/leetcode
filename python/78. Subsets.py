# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 21/6/2020 下午1:00
"""
from typing import List


class Solution:
    def dfs(self, nums, results, idx, cur):
        if idx >= len(nums):
            results.append(cur)
            return

        self.dfs(nums, results, idx + 1, cur)
        self.dfs(nums, results, idx + 1, cur + [nums[idx]])

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        results = []
        self.dfs(nums, results, 0, [])
        return results

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        for n in nums:
            ret += [x + [n] for x in ret]

        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.subsets([1, 2, 3]))
