# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 26/2/2020 上午11:13
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums is None:
            return 0
        if len(nums) <= 1:
            return len(nums)
        cur_idx, next_idx = 0, 1
        while next_idx < len(nums):
            if nums[next_idx] == nums[cur_idx]:
                while next_idx < len(nums) and nums[next_idx] == nums[cur_idx]:
                    next_idx += 1
                if next_idx < len(nums):
                    nums[cur_idx + 1] = nums[next_idx]
                else:
                    break
            cur_idx += 1
            next_idx += 1
            nums[cur_idx] = nums[next_idx - 1]

        return cur_idx + 1


if __name__ == '__main__':
    l = [1, 1, 1, 1, 1, 2, 2, 3, 4, 5, 6]
    s = Solution()
    print(s.removeDuplicates(l))
    print(l)
