# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 27/2/2020 上午12:29
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices is None or len(prices) <= 1:
            return 0

        days = len(prices)
        buy, nonbuy = [0] * days, [0] * days
        buy[0] = -prices[0]

        for i in range(1, days):
            buy[i] = max(nonbuy[i - 1], buy[i - 1] + prices[i]) - prices[i]
            nonbuy[i] = max(nonbuy[i - 1], buy[i - 1] + prices[i])

        return nonbuy[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4, 6, 7, 5, 4, 1]))  # 10
    print(s.maxProfit([4, 6, 7]))  # 3
