//trick
public class Solution
{
    public int HammingWeight(uint n)
    {
        return Convert.ToString(n, 2).Replace("0", "").Length;
    }
}

//
public class Solution
{
    public int HammingWeight(uint n)
    {
        int count = 0;
        while (n > 0)
        {
            count += n % 2 == 0 ? 0 : 1;
            n /= 2;
        }
        return count;
    }
}