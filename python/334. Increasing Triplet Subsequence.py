# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 25/6/2020 下午4:35
"""


class Solution:
    max_n = 2 ** 31

    def increasingTriplet(self, nums: List[int]) -> bool:
        lowest1, lowest2, mid = self.max_n, self.max_n, self.max_n

        for i, n in enumerate(nums):
            if n > mid > lowest1:
                # print(lowest1, mid, n)
                return True

            if n < lowest1 and n < lowest2:
                lowest2 = n

            if lowest1 < n < mid:
                mid = n

            if lowest2 < n <= mid:
                lowest1 = lowest2
                mid = n

        return False
