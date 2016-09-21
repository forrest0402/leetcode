public class Solution
{
    public int StrStr(string haystack, string needle)
    {
        for (int i = 0; i <= haystack.Length - needle.Length; ++i)
        {
            bool flag = true;
            for (int j = 0; j < needle.Length; ++j)
            {
                if (haystack[i + j] != needle[j])
                {
                    flag = false;
                    break;
                }
            }
            if (flag)
                return i;
        }
        return -1;
    }
}