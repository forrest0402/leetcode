public class Solution
{
    public bool IsPowerOfThree(int n)
    {
        if (n == 0)
            return false;
        double ans = Math.Log(n, 3);
        return Math.Min(ans - Math.Floor(ans), Math.Ceiling(ans) - ans) < 1e-10;
    }
}