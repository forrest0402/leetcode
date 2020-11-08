# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 8/11/2020 下午8:47
"""
from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp_items(a, b):
            if a == b:
                return 0

            return 1 if a + b > b + a else -1


        nums = [str(n) for n in nums]
        cmp_items_py3 = cmp_to_key(cmp_items)
        nums.sort(key=cmp_items_py3, reverse=True)
        return str(int(''.join(nums)))


if __name__ == "__main__":
    s = Solution()
    print(s.largestNumber([3, 30, 34, 5, 9]))
