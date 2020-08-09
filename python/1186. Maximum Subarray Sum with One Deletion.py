# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 9/8/2020 下午5:11
"""

from typing import List


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        dpw, dpo = [0 for _ in range(len(arr))], [0 for _ in range(len(arr))]
        dpw[0] = dpo[0] = arr[0]
        ret = arr[0]
        for i in range(1, len(arr)):
            dpw[i] = max(dpw[i - 1] + arr[i], arr[i])
            dpo[i] = max(dpo[i - 1] + arr[i], dpw[i - 1])
            ret = max(dpw[i], dpo[i], ret)

        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.maximumSum([2, 1, -2, -5, -2]))  # 3
    print(s.maximumSum([1, -2, 0, 3, 5, -8, 10, 2, 3, -23, -3, -1, 5, 9, 1]))  # 26
    print(s.maximumSum([1, -2, -2, 3]))  # 3
    print(s.maximumSum([-1, -1, -1, -1]))  # -1
    print(s.maximumSum([1, -2, 0, 3]))  # 4
