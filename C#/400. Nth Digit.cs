public class Solution
{
    long Pow(int n)
    {
        long sum = 1;
        while (--n > 0)
            sum *= 10;
        return sum;
    }
    int Ceil(int a, int b)
    {
        for (int i = 1; i <= a; ++i)
        {
            if (b * i >= a)
                return i;
        }
        return 0;
    }
    int Maxbit(int n)
    {
        int sum = 1;
        while (n-- > 0)
            sum *= 10;
        return sum - 1;
    }
    public int findNthDigit(int n)
    {
        if (n <= 9)
            return n;
        long sum = 0;
        for (int i = 1; i <= 12; ++i)
        {
            sum += i * 9 * Pow(i);
            if (n <= sum)
            {
                sum -= i * 9 * Pow(i);
                int count = (int)(n - sum);
                int number = Ceil(count, i) + Maxbit(i - 1);
                int bit = 0;
                for (int j = 0; j <= i - (count % i == 0 ? i : count % i); ++j)
                {
                    bit = number % 10;
                    number /= 10;
                }
                return bit;
            }
        }
        return -1;
    }
}