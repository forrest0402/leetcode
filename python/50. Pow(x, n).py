# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 16/6/2020 上午12:22
"""


class Solution:

    def myPow2(self, x: float, n: int) -> float:
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

        res = self.myPow2(x, n // 2)
        if n % 2 == 0:
            res *= res
        else:
            res = res * res * x

        return res if flag else 1.0 / res

    def myPow3(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            return 1.0 / self.myPow3(x, -n)

        return self.myPow3(x * x, n // 2) if n % 2 == 0 else x * self.myPow3(x * x, n // 2)

    def myPow(self, x: float, n: int) -> float:
        flag = True
        if n < 0:
            flag = False
            n = -n

        ans, odd = x, 1
        while n > 1:
            if n % 2 != 0:
                odd *= ans
            ans = ans * ans
            n = n // 2

        return ans * odd if flag else 1.0 / (ans * odd)


if __name__ == "__main__":
    s = Solution()
    print(pow(2, -1))
    print(s.myPow(2, -1))
