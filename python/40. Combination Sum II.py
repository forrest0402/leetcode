# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 14/6/2020 下午6:34
"""
from typing import List


class Solution:

    def dfs(self, candidates, i, cur_sum, target, res, combination):
        if cur_sum == target:
            res.append(combination[:])

        if cur_sum >= target or i >= len(candidates):
            return

        for j in range(i, len(candidates)):
            if candidates[j] + cur_sum > target:
                break
            if j > i and candidates[j] == candidates[j - 1]:
                continue
            combination.append(candidates[j])
            self.dfs(candidates, j + 1, cur_sum + candidates[j], target, res, combination)
            combination.pop(-1)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.dfs(candidates, 0, 0, target, res, [])
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum2([2, 5, 2, 1, 2], 5))
