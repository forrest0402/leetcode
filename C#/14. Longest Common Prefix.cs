public class Solution
{
    public string LongestCommonPrefix(string[] strs)
    {
        if (strs.Length == 0 || strs[0] == "")
            return "";
        string ans = "";
        for (int col = 0; col < strs[0].Length; ++col)
        {
            bool flag = true;
            for (int row = 0; row < strs.Length - 1; ++row)
            {
                if (strs[row].Length <= col || strs[row + 1].Length <= col)
                {
                    flag = false;
                    break;
                }
                if (strs[row][col] == strs[row + 1][col])
                    continue;
                flag = false;
                break;
            }
            if (flag)
                ans += strs[0][col] + "";
            else break;
        }
        return ans;
    }
}