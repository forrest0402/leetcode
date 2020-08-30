# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 30/8/2020 下午4:18
"""

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return -1

        if k == len(nums):
            return min(nums)

        if k == 1:
            return max(nums)

        print(nums, k)
        mid = nums[0]
        left, right = [], []

        for i in range(0, len(nums)):
            if nums[i] <= mid:
                left.insert(0, nums[i])
            else:
                right.insert(0, nums[i])

        if len(right) == 0:
            return self.findKthLargest(nums[1:], k - 1)

        if len(right) == k - 1:
            return mid

        if len(right) < k - 1:
            return self.findKthLargest(left, k - len(right))

        return self.findKthLargest(right, k)


if __name__ == "__main__":
    s = Solution()
    print(s.findKthLargest([3, 3, 3, 3, 3, 3, 3, 3, 3], 8))
    print(s.findKthLargest([7, 6, 5, 4, 3, 2, 1], 2))
