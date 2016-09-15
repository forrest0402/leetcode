public class Solution
{
    public bool IsPowerOfFour(int num)
    {
        double ans = Math.Log(num, 4);
        return Math.Min(ans - Math.Floor(ans), Math.Ceiling(ans) - ans) < 1e-10;
    }
}