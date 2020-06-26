# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 26/6/2020 下午11:55
"""
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for __ in range(m + 1)]
        lists = []
        for i, text in enumerate(strs):
            zn, on = 0, 0
            for ch in text:
                if ch == '1':
                    on += 1
                else:
                    zn += 1
            lists.append({
                "1": on,
                "0": zn
            })

        for i in range(0, len(strs)):
            for mm in range(m, -1, -1):
                for nn in range(n, -1, -1):
                    if mm >= lists[i]["0"] and nn >= lists[i]["1"]:
                        dp[mm][nn] = max(dp[mm][nn], dp[mm - lists[i]["0"]][nn - lists[i]["1"]] + 1)

        return dp[m][n]


if __name__ == "__main__":
    s = Solution()
    print(s.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3))  # 4
    print(s.findMaxForm(["10", "0001", "111001", "1", "0"], 1, 1))  # 2
    print(s.findMaxForm(["10", "0001", "111001", "1", "0"], 3, 4))  # 3
