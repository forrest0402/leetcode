public class Solution
{
    public int MaxProfit(int[] prices)
    {
        int[] sell = new int[prices.Length], nosell = new int[prices.Length], dp = new int[prices.Length];
        dp[0] = sell[0] = prices[0];
        int minBuy1 = prices[0], minBuy2 = 0;
        for (int i = 1; i < prices.Length; ++i)
        {
            dp[i - 1] = Math.Max(sell[i - 1], nosell[i - 1]);
            sell[i] = prices[i] > minBuy1 ? nosell[i - 1] + prices[i] - minBuy1 : nosell[i - 1];
            if (sell[i - 1] > nosell[i - 1])
            {
                nosell[i] = sell[i - 1];
                minBuy1 = minBuy2;
            }
            else
                nosell[i] = nosell[i - 1];
            if (minBuy1 > prices[i])
                minBuy1 = prices[i];
        }
        return Math.Max(sell[prices.Length - 1], nosell[prices.Length - 1]);
    }
}