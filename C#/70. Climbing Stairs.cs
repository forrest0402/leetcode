public class Solution
{
    public double Factorial(int n)
    {
        double ans = 1;
        for (int i = 2; i <= n; ++i)
            ans *= i;
        return ans;
    }
    public int ClimbStairs(int n)
    {
        double count = 0;
        int step1 = n, step2 = 0;
        while (step1 >= 0)
        {
            count += Factorial(step1 + step2) / (Factorial(step1) * Factorial(step2));
            step1 -= 2;
            ++step2;
        }
        return (int)count;
    }
}