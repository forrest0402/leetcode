# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 16/6/2020 上午12:22
"""


class Solution:

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n == 1:
            return x
        if n == -1:
            return 1.0 / x

        flag = True
        if n < 0:
            flag = False
            n = -n

        res = self.myPow(x, n // 2)
        if n % 2 == 0:
            res *= res
        else:
            res = res * res * x

        return res if flag else 1.0 / res


if __name__ == "__main__":
    pass
