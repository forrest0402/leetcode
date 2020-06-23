# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 23/6/2020 下午3:10
"""


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        ret = 0
        for i in range(0, 32):
            if n == 0 or m == 0:
                break

            if n == m and n & 1 == 1:
                ret += 2 ** i

            n = n >> 1
            m = m >> 1

        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.rangeBitwiseAnd(16, 17))
