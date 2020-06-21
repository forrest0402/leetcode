# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 21/6/2020 下午9:08
"""

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        dup = set()
        nums.sort()
        for n in nums:
            cur = []
            for x in ret:
                v = x + [n]
                key = '-'.join(map(str, v))
                if key not in dup:
                    dup.add(key)
                    cur.append(v)
            ret += cur

        return ret
