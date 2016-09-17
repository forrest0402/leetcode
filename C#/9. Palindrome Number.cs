public class Solution
{
    int Pow(int n)
    {
        int sum = 1;
        while (n-- > 0)
            sum *= 10;
        return sum;
    }
    public bool IsPalindrome(int x)
    {
        if (x < 0)
            return false;
        int length = 0, num = x, y = 0;
        while (num > 0)
        {
            num /= 10;
            ++length;
        }
        num = x;
        while (num > 0)
        {
            y += num % 10 * Pow(--length);
            num /= 10;
        }
        return y == x;
    }
}