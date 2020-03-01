# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 28/2/2020 上午3:18
"""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        num = bin(num)[2:]
        return len(num) + num.count('1') - 1


if __name__ == "__main__":
    s = Solution()
    print(s.numberOfSteps(0))
