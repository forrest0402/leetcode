# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 26/3/2020 上午12:00
"""
from typing import List
import random


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min_idx, min_n = 0, 2147483647
        for i, n in enumerate(nums):
            if n < min_n:
                min_n = n
                min_idx = i

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid] <= nums[right]:
                if target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif min_idx > mid:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


if __name__ == "__main__":
    s = Solution()
    assert s.search([4], 4) == 0
    assert s.search([16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 0) == 4
    assert s.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert s.search([4, 5, 6, 7, 0, 1, 2], 3) == -1

    while True:
        start = random.randint(10, 20)
        end = random.randint(start + 1, 30)
        array = [x for x in range(start, end)] + [x for x in range(start)]
        print(array)
        for i, x in enumerate(array):
            assert s.search(array, x) == i
