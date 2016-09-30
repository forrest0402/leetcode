public class Solution
{
    public int BulbSwitch(int n)
    {
        int count = 0, num = 0;
        while (num * num < n)
        {
            ++count;
            ++num;
        }
        if (num * num == n)
            return count;
        return count - 1;
    }
}