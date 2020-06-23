# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 23/6/2020 下午10:55
"""

from typing import List


class Solution:

    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        c1, c2 = None, None
        n1, n2 = 0, 0
        for val in nums:

            if val == c1:
                n1 += 1
                continue

            if val == c2:
                n2 += 1
                continue

            if n1 == 0:
                c1 = val
                n1 = 1
                continue

            if n2 == 0:
                c2 = val
                n2 = 1
                continue

            # three different numbers
            n1 -= 1
            n2 -= 1

        n1 = n2 = 0
        for n in nums:
            if n == c1:
                n1 += 1
            elif n == c2:
                n2 += 1

        t = len(nums) // 3

        return [x for i, x in enumerate([c1, c2]) if [n1, n2][i] > t]


if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([1, 2, 2, 3, 2, 1, 1, 3]))
    print(s.majorityElement([1, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 1, 6, 6, 6, 6, 6, 6, 1, 1, 1, 6, 7, 1]))
