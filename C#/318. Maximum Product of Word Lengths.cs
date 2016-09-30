public class Solution
{
    public int MaxProduct(string[] words)
    {
        if (words == null || words.Length == 1)
            return 0;
        int maxL = 0;
        List<bool[]> list = new List<bool[]>();
        foreach (string strw in words)
        {
            bool[] v = new bool['z' - 'a' + 1];
            foreach (char chw in strw)
                v[chw - 'a'] = true;
            list.Add(v);
        }
        for (int i = 0; i < list.Count; ++i)
        {
            for (int j = i + 1; j < list.Count; ++j)
            {
                bool flag = true;
                for (int k = 0; k < 'z' - 'a' + 1; ++k)
                {
                    if (list[i][k] && list[j][k])
                    {
                        flag = false;
                        break;
                    }
                }
                if (flag && words[i].Length * words[j].Length > maxL)
                    maxL = words[i].Length * words[j].Length;
            }
        }
        return maxL;
    }
}

//a better solution
public class Solution
{
    public int MaxProduct(string[] words)
    {
        if (words == null || words.Length == 1)
            return 0;
        int maxL = 0, count = 0;
        int[] list = new int[words.Length];
        foreach (string strw in words)
        {
            foreach (char chw in strw)
                list[count] |= 1 << chw - 'a';
            ++count;
        }
        for (int i = 0; i < list.Length; ++i)
        {
            for (int j = i + 1; j < list.Length; ++j)
            {
                if (((list[i] & list[j]) == 0) && words[i].Length * words[j].Length > maxL)
                    maxL = words[i].Length * words[j].Length;
            }
        }
        return maxL;
    }
}