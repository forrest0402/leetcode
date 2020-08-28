# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 16/8/2020 下午9:51
"""
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        idx = 0
        while True:

            if idx >= len(nums):
                break

            if nums[idx] == idx + 1 or nums[nums[idx] - 1] == nums[idx]:
                idx += 1
                continue

            tmp = nums[nums[idx] - 1]
            nums[nums[idx] - 1] = nums[idx]
            nums[idx] = tmp
            print(nums)

        ret = []
        for i, n in enumerate(nums):
            if n != i + 1:
                ret.append(i+1)

        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
