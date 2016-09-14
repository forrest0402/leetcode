public class Solution
{
    Dictionary<char, int> dic = new Dictionary<char, int>{
        {'I',1}, {'V',5}, {'X',10}, {'L',50}, {'C',100}, {'D',500}, {'M',1000}
    };
    public int RomanToInt(string s)
    {
        int count = 0;
        char pre = 'M';
        foreach (char chs in s)
        {
            count += dic[chs];
            if (dic[chs] > dic[pre])
            {
                count -= 2 * dic[pre];
            }
            pre = chs;
        }
        return count;
    }
}