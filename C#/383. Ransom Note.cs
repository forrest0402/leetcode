public class Solution
{
    public bool CanConstruct(string ransomNote, string magazine)
    {
        bool[] used = new bool[magazine.Length];
        for (int i = 0; i < ransomNote.Length; ++i)
        {
            bool flag = false;
            for (int j = 0; j < magazine.Length; ++j)
            {
                if (!used[j] && magazine[j] == ransomNote[i])
                {
                    flag = true;
                    used[j] = true;
                    break;
                }
            }
            if (!flag)
                return false;
        }
        return true;
    }
}