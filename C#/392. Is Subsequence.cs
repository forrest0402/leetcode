public class Solution
{
    public bool IsSubsequence(string s, string t)
    {
        if (s == "")
            return true;
        bool flag = false;
        int index = 0, find = 0;
        foreach (char chs in s)
        {
            bool hasFind = false;
            while (index < t.Length)
            {
                if (t[index++] == chs)
                {
                    hasFind = true;
                    break;
                }
            }
            if (hasFind)
                ++find;
            else break;
            if (find == s.Length)
                flag = true;
        }
        return flag;
    }
}

//
public class Solution
{
    public bool IsSubsequence(string s, string t)
    {
        int prev = 0;
        foreach (char chs in s)
        {
            prev = t.IndexOf(chs, prev);
            if (prev == -1)
                return false;
            ++prev;
        }
        return true;
    }
}