# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 23/6/2020 下午4:56
"""
from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        ret = s + 1
        start, step, sum = 0, 0, 0
        for i, n in enumerate(nums):
            sum += n
            step += 1
            while sum - nums[start] >= s:
                sum -= nums[start]
                start += 1
                step -= 1

            if sum >= s:
                ret = min(step, ret)

        return ret if ret < s + 1 else 0


if __name__ == "__main__":
    s = Solution()
    print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
