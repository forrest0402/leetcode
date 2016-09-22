public class Solution
{
    bool IsLegal(char ch)
    {
        return (ch >= 'a' && ch <= 'z') || (ch >= '0' && ch <= '9') || (ch >= 'A' && ch <= 'Z');
    }
    public bool IsPalindrome(string s)
    {
        int lPos = 0, rPos = s.Length - 1;
        while (lPos < rPos)
        {
            while (lPos < s.Length && !IsLegal(s[lPos]))
                ++lPos;
            while (rPos >= 0 && !IsLegal(s[rPos]))
                --rPos;
            if (lPos >= rPos)
                break;
            if (Char.ToLower(s[lPos++]) != Char.ToLower(s[rPos--]))
                return false;
        }
        return true;
    }
}
//
public class Solution
{
    bool IsLegal(char ch)
    {
        return (ch >= 'a' && ch <= 'z') || (ch >= '0' && ch <= '9') || (ch >= 'A' && ch <= 'Z');
    }
    public bool IsPalindrome(string s)
    {
        int lPos = 0, rPos = s.Length - 1;
        while (lPos < rPos)
        {
            while (lPos < s.Length && !IsLegal(s[lPos]))
                ++lPos;
            while (rPos >= 0 && !IsLegal(s[rPos]))
                --rPos;
            if (lPos >= rPos)
                break;
            if ((s[lPos] == s[rPos]) || (s[rPos] >= 'a' && s[rPos] <= 'z' && s[lPos] == s[rPos] + 'A' - 'a') || (s[rPos] >= 'A' && s[rPos] <= 'Z' && s[lPos] == s[rPos] - 'A' + 'a'))
            {
                ++lPos;
                --rPos;
                continue;
            }
            return false;
        }
        return true;
    }
}