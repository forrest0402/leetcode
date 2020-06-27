# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 27/6/2020 下午10:03
"""

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1

        if not coins:
            return 0

        dp = [0 for _ in range(amount + 1)]
        for i in range(amount + 1):
            dp[i] = 1 if i % coins[0] == 0 else 0

        for i in range(1, len(coins)):
            for s in range(amount, -1, -1):
                k = s // coins[i]
                while k > 0:
                    dp[s] += dp[s - k * coins[i]]
                    k -= 1

        return dp[amount]


if __name__ == "__main__":
    s = Solution()
    print(s.change(11, [10]))
