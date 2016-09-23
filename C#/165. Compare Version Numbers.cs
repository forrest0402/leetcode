public class Solution
{
    public int CompareString(string s1, string s2)
    {
        int len = s1.Length > s2.Length ? s1.Length : s2.Length;
        s1 = s1.PadLeft(len, '0');
        s2 = s2.PadLeft(len, '0');
        if (s1 == s2)
            return 0;
        for (int i = 0; i < len; ++i)
        {
            if (s1[i] < s2[i])
                return -1;
            if (s1[i] > s2[i])
                return 1;
        }
        return 1;
    }
    public int CompareVersion(string version1, string version2)
    {
        if (version1.Length == 0 && version2.Length > 0)
            return -1;
        if (version2.Length == 0 && version1.Length > 0)
            return 1;
        List<string> v1 = version1.Split('.').ToList();
        List<string> v2 = version2.Split('.').ToList();
        while (v2.Count - v1.Count > 0)
            v1.Add("0");
        while (v1.Count - v2.Count > 0)
            v2.Add("0");
        for (int i = 0; i < v1.Count; ++i)
        {
            int cmp = CompareString(v1[i], v2[i]);
            if (cmp == 1)
                return 1;
            if (cmp == -1)
                return -1;
        }
        return 0;
    }
}