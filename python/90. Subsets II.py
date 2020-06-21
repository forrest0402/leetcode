# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 21/6/2020 下午9:08
"""

from typing import List


class Solution:
    def subsetsWithDup2(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        nums.sort()
        for i, n in enumerate(nums):
            if i == 0 or n != nums[i - 1]:
                l = len(ret)
            for j in range(len(ret) - l, len(ret)):
                ret.append(ret[j] + [n])
        return ret

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


if __name__ == '__main__':
    s = Solution()
    print(s.subsetsWithDup2([1, 2, 2]))
