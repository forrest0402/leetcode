public class Solution
{
    public bool IsAnagram(string s, string t)
    {
        char[] chars = s.ToCharArray();
        char[] chart = t.ToCharArray();
        Array.Sort(chars);
        Array.Sort(chart);
        return new string(chars) == new string(chart);
    }
}