# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 28/2/2020 下午2:53
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        res, cnt = 0, 0
        while n > 0:
            if n & 1 == 1:
                res += 2 ** (31 - cnt)
            n = n >> 1
            cnt += 1
        return res
