# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 25/6/2020 上午12:08
"""

from typing import List


class Solution:
    max_n = 2 ** 31

    def dfs(self, coins, amount, cache):
        if amount == 0:
            return 0

        if amount < 0:
            return self.max_n

        if amount % coins[0] == 0:
            return amount // coins[0]

        if amount in cache:
            return cache[amount]

        ret = self.max_n
        for coin in coins:
            if coin > amount:
                continue
            value = self.dfs(coins, amount - coin, cache) + 1
            if value < ret:
                ret = value

        cache[amount] = ret
        return ret

    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        cache = dict()
        for coin in coins:
            cache[coin] = 1
        ret = self.dfs(coins, amount, cache)
        return -1 if ret == self.max_n else ret


if __name__ == "__main__":
    s = Solution()
    # print(s.coinChange([3, 6, 9, 13, 14, 16, 19, 30], 70))  # 4
    print(s.coinChange([1, 2, 5], 11))
    # assert s.coinChange([186], 187) == -1
    # assert s.coinChange([186, 419, 83, 408], 6249) == 20
    print(s.coinChange([3, 7, 405, 436], 8839))
    # assert s.coinChange([3, 7, 405, 436], 8839) == 25
