# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 16/6/2020 上午1:34
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        i = 0
        while i < len(nums):
            if nums[i] == 0:
                break
            maxi = 0
            for j in range(i + 1, min(i + nums[i] + 1, len(nums))):
                if nums[j] + j > maxi:
                    maxi = nums[j] + j
                    i = j

            if maxi >= len(nums) - 1:
                return True

        return False


if __name__ == "__main__":
    s = Solution()
    print(s.canJump([2, 3, 1, 1, 4]))
