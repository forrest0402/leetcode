class Solution
{
    public:
    int maxProfit(vector<int>& prices)
    {
        int n = prices.size();
        if (n <= 1) return 0;
        vector<int> dp(n,0);
        int minPrice = prices[0], res = 0;
        for (int i = 1; i < n; ++i)
        {
            minPrice = min(minPrice, prices[i]);
            if (prices[i] - minPrice >= dp[i - 1]) dp[i] = prices[i] - minPrice;
            else
            {
                minPrice = prices[i];
                res += dp[i - 1];
            }
        }

        return res + dp[n - 1];
    }
};