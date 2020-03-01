# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 1/3/2020 下午11:50
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b & 0xffffffff > 0:
            carry = (a & b) << 1
            a ^= b
            b = carry
        return a & 0xffffffff if b > 0 else a


if __name__ == "__main__":
    s = Solution()
    print(s.getSum(-1, 2))
    print(s.getSum(-1, 0))
    print(s.getSum(-1, 1))
    print(s.getSum(-100, 10))
