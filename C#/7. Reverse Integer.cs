public class Solution
{
    public int Reverse(int x)
    {
        long n = x;
        bool flag = x > 0;
        n = Math.Abs(n);
        char[] array = n.ToString().ToCharArray();
        Array.Reverse(array);
        long ans = long.Parse(new string(array));
        if ((flag && ans > int.MaxValue) || (!flag && -ans < int.MinValue))
            return 0;
        return flag ? int.Parse(new string(array)) : -int.Parse(new string(array));
    }
}