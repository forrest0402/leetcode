# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 28/2/2020 上午11:51
"""
import math


class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        x = int(math.log(n, 5))
        for i in range(2, x + 1):
            res += n // (5 ** i)
        return n // 5 + res

    def raw(self, n):
        res = 0
        while n >= 5:
            res += n // 5
            n //= 5
        return res


if __name__ == "__main__":
    s = Solution()
    n = 4
    print('actual: {}; expected:{}'.format(s.trailingZeroes(n), s.raw(n)))
    assert s.trailingZeroes(n) == s.raw(n)
