public class Solution
{
    public int MaxProfit(int[] prices)
    {
        int maxProfit = 0, minBuy = int.MaxValue;
        for (int i = 0; i < prices.Length; ++i)
        {
            if (prices[i] - minBuy > maxProfit)
                maxProfit = prices[i] - minBuy;
            if (prices[i] < minBuy)
                minBuy = prices[i];
        }
        return maxProfit;
    }
}