public class Solution
{
    public bool IsHappy(int n)
    {
        HashSet<int> set = new HashSet<int>();
        while (n != 1)
        {
            if (set.Contains(n))
                break;
            set.Add(n);
            int sum = 0;
            while (n > 0)
            {
                sum += (n % 10) * (n % 10);
                n /= 10;
            }
            n = sum;
        }
        return n == 1;
    }
}