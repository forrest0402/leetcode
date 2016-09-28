public class Solution
{
    public int CountNumbersWithUniqueDigits(int n)
    {
        if (n == 0)
            return 1;
        int count = 10;
        for (int i = 1; i < n; ++i)
        {
            int num = 9;
            for (int j = 1; j <= i; ++j)
                num *= (10 - j);
            if (num < 0)
                num = 0;
            count += num;
        }
        return count;
    }
}