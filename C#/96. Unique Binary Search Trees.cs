﻿public class Solution
{
    public int NumTrees(int n)
    {
        int[] dp = new int[n + 1];
        dp[0] = dp[1] = 1;
        for (int i = 2; i <= n; ++i)
            for (int j = i - 1; j >= 0; --j)
                dp[i] += dp[j] * dp[i - 1 - j];
        return dp[n];
    }
}