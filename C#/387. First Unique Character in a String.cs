public class Solution
{
    public int FirstUniqChar(string s)
    {
        int[] visited = new int[(int)'z' + 1];
        for (int i = 0; i < visited.Length; ++i)
            visited[i] = -1;
        for (int i = 0; i < s.Length; ++i)
        {
            if (visited[(int)s[i]] == -2)
                continue;
            if (visited[(int)s[i]] == -1)
                visited[(int)s[i]] = i;
            else visited[(int)s[i]] = -2;
        }
        int index = int.MaxValue;
        foreach (int i in visited)
            if (i >= 0 && i < index)
                index = i;
        return index == int.MaxValue ? -1 : index;
    }
}