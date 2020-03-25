# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 25/3/2020 下午10:39
"""

import random


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if divisor == dividend:
            return 1
        if divisor == -dividend:
            return -1

        positive = True
        if (dividend < 0 < divisor) or (dividend > 0 > divisor):
            dividend = -dividend
            positive = False
        if dividend < 0 and divisor < 0:
            dividend, divisor = -dividend, -divisor

        if dividend < divisor:
            return 0

        count = 2
        step = [divisor]
        h_count = [1]
        n = divisor + divisor
        while n < dividend:
            if n + n > dividend:
                break
            step.append(n)
            h_count.append(count)
            n += n
            count += count

        idx = len(step) - 1
        while n <= dividend:
            while idx >= 0 and n + step[idx] > dividend:
                idx -= 1
            if idx < 0:
                break

            n += step[idx]
            count += h_count[idx]

        if n > dividend:
            count -= 1
        if count > 2147483647 and positive:
            count = 2147483647

        if not positive:
            return -count;

        return count

    def divide2(self, dividend: int, divisor: int) -> int:

        if (divisor < 0 and dividend > 0) or (divisor > 0 and dividend < 0):
            res = -(-dividend // divisor)
        else:
            res = dividend // divisor

        if res > 2147483647:
            res = 2147483647

        return res


if __name__ == "__main__":
    s = Solution()
    assert s.divide(2147483648, -1) == -2147483648
    assert s.divide(1026117192, -874002063) == -1
    while True:
        a = random.randint(-100000, 100000)
        b = random.randint(-10000, 10000)
        print(a, b)
        if b == 0:
            continue
        assert s.divide(a, b) == s.divide2(a, b)
