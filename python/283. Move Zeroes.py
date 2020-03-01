# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 1/3/2020 下午7:18
"""


class Solution:

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums is None:
            return
        count, i = 0, 0
        while i < len(nums):
            if nums[i] == 0:
                count += 1
            elif count > 0:
                nums[i - count] = nums[i]
                nums[i] = 0
            i += 1
