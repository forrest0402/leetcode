# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 9/8/2020 下午3:30
"""
from typing import List


class Solution:
    def minus(self, A: List[int]) -> int:
        dpi, dpj = [0 for _ in range(len(A))], [0 for _ in range(len(A))]
        dpi[1], dpj[1] = A[1] - A[0] + 1, A[0] - A[1] + 1
        ret = max(dpi[1], dpj[1])
        for i in range(2, len(A)):
            dpi[i] = max(dpi[i - 1] + 1 + A[i] - A[i - 1], A[i] - A[i - 1] + 1)
            dpj[i] = max(dpj[i - 1] + 1 - A[i] + A[i - 1], A[i - 1] - A[i] + 1)
            ret = max(dpi[i], dpj[i], ret)

        return ret

    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        a = self.minus([arr1[i] + arr2[i] for i in range(len(arr1))])
        b = self.minus([-arr1[i] - arr2[i] for i in range(len(arr1))])
        c = self.minus([arr1[i] - arr2[i] for i in range(len(arr1))])
        d = self.minus([-arr1[i] + arr2[i] for i in range(len(arr1))])
        return max(a, b, c, d)


if __name__ == "__main__":
    s = Solution()
    print(s.maxAbsValExpr([1, -2, -5, 0, 10], [0, -2, -1, -7, -4]))  # 20
    print(s.maxAbsValExpr([1, 2, 3, 4], [-1, 4, 5, 6]))  # 13
