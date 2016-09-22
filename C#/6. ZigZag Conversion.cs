public class Solution
{
    public string Convert(string s, int numRows)
    {
        if (s == "")
            return "";
        if (numRows < 2)
            return s;
        char[,] array = new char[s.Length + 1, numRows];
        int count = 0, pi = 0, pj = 0;
        while (count < s.Length)
        {
            array[pi, pj] = s[count++];
            if (pi % 2 == 0)
                ++pj;
            else --pj;
            if (pi % 2 == 0 && pj == numRows)
            {
                pj -= 2;
                ++pi;
            }
            if (pi % 2 == 1 && pj == 0)
            {
                ++pi;
            }
        }
        string ans = "";
        for (int j = 0; j < numRows; ++j)
        {
            for (int i = 0; i < pi; ++i)
            {
                if (array[i, j] != '\0')
                    ans += array[i, j] + "";
            }
        }
        return ans;
    }
}