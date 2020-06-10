# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 10/6/2020 下午11:50
"""

from typing import List


class Solution:
    digit_map = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }

    def dfs(self, digits, i, com, results):
        if len(com) == len(digits):
            if len(com) > 0:
                results.append(com)
            return

        for d in self.digit_map[digits[i]]:
            self.dfs(digits, i + 1, com + d, results)

    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        try:
            self.dfs(digits, 0, '', res)
        except:
            return []
        return res


if __name__ == "__main__":
    s = Solution()
    res = s.letterCombinations('23')
    print(res)
