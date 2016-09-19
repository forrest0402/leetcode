public class Solution
{
    public string CountAndSay(int n)
    {
        List<char> chars = new List<char> { '1' };
        for (int i = 1; i < n; ++i)
        {
            for (int j = 0; j < chars.Count; ++j)
            {
                char temp = chars[j];
                int k = j;
                while (k < chars.Count && chars[k] == temp) ++k;
                chars[j] = Convert.ToChar(k - j + '0');
                chars.Insert(++j, temp);
                for (int l = 0; l < k - j; ++l)
                    chars.RemoveAt(j + 1);
            }
        }
        return new string(chars.ToArray());
    }
}