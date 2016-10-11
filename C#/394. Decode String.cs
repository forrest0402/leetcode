public class Solution
{
    int index = 0;
    string s = "";
    private void Expand(StringBuilder ans, int k)
    {
        string nStr = "";
        StringBuilder str = new StringBuilder();
        for (index += 1; index < s.Length; ++index)
        {
            if (s[index] == ']')
            {
                for (int i = 0; i < k; ++i)
                    ans.Append(str);
                return;
            }
            if (s[index] == '[')
            {
                Expand(str, int.Parse(nStr));
                nStr = "";
            }
            else if (s[index] <= '9' && s[index] >= '0')
                nStr += s[index];
            else
                str.Append(s[index]);
        }
    }
    public string DecodeString(string s)
    {
        StringBuilder ans = new StringBuilder();
        string nStr = "";
        this.s = s;
        for (index = 0; index < s.Length; ++index)
        {
            if (s[index] == '[')
            {
                Expand(ans, int.Parse(nStr));
                nStr = "";
            }
            else if (s[index] <= '9' && s[index] >= '0')
                nStr += s[index];
            else ans.Append(s[index]);
        }
        return ans.ToString();
    }
}