# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 11/7/2020 下午9:01
"""


class RLEIterator:

    def __init__(self, A: List[int]):
        self.nums, self.cons = [], []
        count = 0
        for i, n in enumerate(A):
            if i % 2 == 0:
                if n > 0:
                    self.cons.append(count)
                    count += n
            else:
                if A[i - 1] > 0:
                    self.nums.append(n)

        self.cons.append(count)
        self.nums.append(-1)
        self.idx = 0
        self.last = self.nums[0]

    def next(self, n: int) -> int:
        if n == 0:
            return self.last

        self.idx += n
        if self.idx > self.cons[-1]:
            return -1

        left, right = 0, len(self.cons) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.cons[mid] == self.idx - 1:
                break

            if self.cons[mid] < self.idx - 1:
                left = mid + 1
            else:
                right = mid - 1

        # print(n, mid)

        if self.cons[mid] > self.idx - 1:
            mid -= 1

        self.last = self.nums[mid]
        return self.last
