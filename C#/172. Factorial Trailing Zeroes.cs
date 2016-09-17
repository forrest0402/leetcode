// SUM(N/5^1,  N/5^2, N/5^3...)
public class Solution
{
    public int TrailingZeroes(int n)
    {
        return n == 0 ? 0 : n / 5 + TrailingZeroes(n / 5);
    }
}