# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 24/6/2020 下午4:11
"""
import math


class Solution:

    def numSquares(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        f = math.floor(math.sqrt(n))
        n -= f * f
        return self.numSquares(n) + 1


if __name__ == "__main__":
    s = Solution()
    print(s.numSquares(1000))
