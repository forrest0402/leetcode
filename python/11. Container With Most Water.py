# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 15/3/2020 下午5:36
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        idx1, idx2 = 0, len(height) - 1
        while idx1 < idx2:
            res = max(res, min(height[idx1], height[idx2]) * (idx2 - idx1))
            if height[idx1] > height[idx2]:
                idx2 -= 1
            else:
                idx1 += 1

        return res
