# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 9/8/2020 下午11:40
"""

from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        m = dict()
        dp = [0 for _ in range(len(arr))]
        ret = 1
        for i, e in enumerate(arr):
            if e - difference in m:
                dp[i] = dp[m[e - difference]] + 1
            else:
                dp[i] = 1
            m[e] = i
            ret = max(ret, dp[i])
        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.longestSubsequence([1, 2, 3, 4, 5, 6, 8], 1))
    print(s.longestSubsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], -2))
