# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 26/2/2020 下午12:10
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0
        max_sum, sum = -2 ** 31, 0
        for n in nums:
            sum += n
            if sum > max_sum:
                max_sum = sum
            if sum < 0:
                sum = 0
        return max_sum


if __name__ == "__main__":
    s = Solution()
    print(s.maxSubArray([-2147483647]))
