# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 23/6/2020 上午11:51
"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        ret = nums[0]

        sums = [1]

        for n in nums:

            if n == 0:
                sums = [1]
                ret = max(ret, 0)
            else:
                for i in range(len(sums)):
                    sums[i] *= n
                    ret = max(ret, sums[i], n)

            if n < 0:
                if len(sums) >= 4:
                    sums = [max(sums), min(sums), 1]
                else:
                    sums.append(1)

        return ret
