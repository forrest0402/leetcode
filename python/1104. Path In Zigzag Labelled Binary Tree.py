# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 9/8/2020 上午12:14
"""
import math
from typing import List


class Solution:
    def parent(self, num):
        l = math.floor(math.log2(num))
        if l & 1 == 0:
            pre_n = (num - 2 ** l) // 2
            p = 2 ** l - 1 - pre_n
        else:
            pre_n = (2 ** (l + 1) - 1 - num) // 2
            p = 2 ** (l - 1) + pre_n
        return p

    def pathInZigZagTree(self, label: int) -> List[int]:
        ret = [label]
        while True:
            if label == 1:
                break
            label = self.parent(label)
            ret.insert(0, label)

        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.pathInZigZagTree(26))
