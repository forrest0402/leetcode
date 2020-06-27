# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 28/6/2020 上午1:35
"""
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        class Solution:
            def subarraySum(self, nums: List[int], k: int) -> int:
                sum, ret = 0, 0
                dicts = dict()
                dicts[0] = 1
                for n in nums:

                    sum += n
                    key = sum - k
                    if sum - k in dicts:
                        ret += dicts[key]

                    dicts[sum] = 1 if sum not in dicts else dicts[sum] + 1

                return ret


if __name__ == "__main__":
    s = Solution()
    print(s.subarraySum([0, 0, 0], 0))
