# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 28/2/2020 上午2:41
"""


class Solution:
    def valid(self, c):
        return ('z' >= c >= 'a') or ('9' >= c >= '0')

    def isPalindrome(self, s: str) -> bool:
        if s is None or s == '' or len(s) == 1:
            return True

        idx1, idx2 = 0, len(s) - 1
        s = s.lower()
        while idx1 < idx2:
            while idx1 < idx2 and not self.valid(s[idx1]):
                idx1 += 1
            while idx1 < idx2 and not self.valid(s[idx2]):
                idx2 -= 1

            if s[idx1] != s[idx2]:
                return False
            idx1 += 1
            idx2 -= 1
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome('5 6 6 $# 7 5'))
