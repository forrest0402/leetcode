# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 30/8/2020 下午4:51
"""
import json
import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return -1

        if k == len(nums):
            return min(nums)

        if k == 1:
            return max(nums)

        if max(nums) == min(nums):
            return nums[0]

        # print(nums, k)
        idx = random.randint(0, len(nums) - 1)
        mid = nums[idx]
        left, right = [], []

        for i in range(0, len(nums)):
            if nums[i] <= mid:
                left.insert(0, nums[i])
            else:
                right.insert(0, nums[i])

        if len(right) == 0:
            return self.findKthLargest(nums[:idx] + nums[idx + 1:], k - 1)

        if len(right) == k - 1:
            return mid

        if len(right) < k - 1:
            return self.findKthLargest(left, k - len(right))

        return self.findKthLargest(right, k)

    def split(self, nums: List[int]):

        topk = self.findKthLargest(nums, len(nums) // 2)
        # print(topk)
        left, right, topn = [], [], 0
        for n in nums:
            if n < topk:
                left.append(n)
            elif n > topk:
                right.append(n)
            else:
                topn += 1

        while topn > 0:
            if len(left) > len(right):
                right.append(topk)
            else:
                left.append(topk)
            topn -= 1

        left.sort(reverse=True)
        right.sort(reverse=True)
        # print(len(left), len(right))
        return left, right

    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        left, right = self.split(nums)
        for i in range(len(nums)):
            if i & 1 == 0:
                nums[i] = (left[i // 2])
            else:
                nums[i] = (right[i // 2])


if __name__ == "__main__":
    s = Solution()
    with open('324', 'r') as fr:
        for line in fr.readlines():
            nums = json.loads(line.strip('\n'))
            s.wiggleSort(nums)
            print(nums)

    nums = [1, 3, 2, 2, 3, 1]
    s.wiggleSort(nums)
    print(nums)
