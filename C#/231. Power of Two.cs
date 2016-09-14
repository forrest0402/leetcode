public class Solution
{
    public bool IsPowerOfTwo(int n)
    {
        if (n == 0)
            return false;
        double ans = Math.Log(n) / Math.Log(2);
        return ans - (int)ans < 1e-10;
    }
}