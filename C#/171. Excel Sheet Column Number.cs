public class Solution
{
    public int TitleToNumber(string s)
    {
        int count = 0;
        for (int i = s.Length - 1; i >= 0; --i)
        {
            count += (s[i] - 'A' + 1) * (int)Math.Pow(26, s.Length - i - 1);
        }
        return count;
    }
}