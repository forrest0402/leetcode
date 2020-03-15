# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 15/3/2020 下午10:27
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s is None or len(s) == 0:
            return ''

        res = s[0]
        max_len = 1

        p = [[False for __ in range(len(s))] for _ in range(len(s))]
        p[0][0] = True
        for k in range(1, len(s)):
            i, j = 0, k
            flag = True
            p[k - 1][k - 1] = True
            p[k - 1][k] = (s[k - 1] == s[k])
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                    continue
                flag = False
                break

            p[0][k] = flag
            if p[k - 1][k]:
                res = s[k - 1:k + 1]
                max_len = 2

        for i in range(len(s) - 2, -1, -1):
            for j in range(1, len(s)):
                if i + 1 >= j:
                    continue
                p[i][j] = p[i + 1][j - 1] and s[i] == s[j]
                if p[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    res = s[i:j + 1]

        return res


if __name__ == "__main__":
    s = Solution()
    assert s.longestPalindrome("babad") == 'aba'
    assert s.longestPalindrome("aaaaaaab") == 'aaaaaaa'
