# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 18/6/2020 上午1:32
"""

import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        result, nums = [], [x for x in range(1, n + 1)]

        while n > 0:
            round = math.factorial(n - 1)
            i = math.ceil(k / round)
            k = k % round
            result.append(nums[i - 1])
            nums.pop(i - 1)
            n -= 1

        return ''.join(map(str, result))


if __name__ == "__main__":
    s = Solution()
    print(s.getPermutation(4, 9))
