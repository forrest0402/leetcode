# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 24/6/2020 下午11:00
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        sell, buy = [0 for _ in range(len(prices))], [0 for _ in range(len(prices))]
        buy[0] = -prices[0]
        buy_max = buy[0]
        sell_max = 0
        for i in range(1, len(prices)):
            buy[i] = sell_max - prices[i]
            sell[i] = max(buy_max + prices[i], sell[i - 2])

            buy_max = max(buy[i], buy_max)
            sell_max = max(sell[i - 1], sell_max)

        # print(sell)
        return max(sell[-1], sell[-2])
