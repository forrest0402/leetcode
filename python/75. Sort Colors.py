# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 21/6/2020 上午1:00
"""

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        start, end, i = 0, len(nums) - 1, 0
        while i <= end:
            if nums[i] == 0:
                nums[i], nums[start] = nums[start], nums[i]
                if i != start and (nums[i] == 2 or nums[i] == 0):
                    i -= 1
                start += 1

            if nums[i] == 2:
                nums[i], nums[end] = nums[end], nums[i]
                end -= 1
                if nums[i] == 0 or nums[i] == 2:
                    i -= 1

            i += 1


if __name__ == "__main__":
    s = Solution()
    l = [2, 0, 1]
    s.sortColors(l)
    print(l)
