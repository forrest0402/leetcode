public class Solution
{
    public string ConvertToTitle(int n)
    {
        string ans = "";
        if (n == 1)
            return "A";
        while (n > 0)
        {
            int remainder = n % 26;
            n /= 26;
            if (remainder == 0)
                --n;
            ans = remainder == 0 ? 'Z' + ans : (char)(remainder - 1 + 'A') + ans;
        }
        return ans;
    }
}