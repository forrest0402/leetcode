public class Solution
{
    public int[] CountBits(int num)
    {
        int[] ans = new int[num + 1];
        int initial = 0;
        for (int i = 0; i <= num; ++i)
        {
            ans[i] = Convert.ToString(i, 2).Replace("0", "").Length;
        }
        return ans;
    }
}

//
public class Solution
{
    public int[] CountBits(int num)
    {
        int[] ans = new int[num + 1];
        int[] bit = new int[32];
        int count = 0;
        for (int i = 0; i <= num; ++i)
        {
            ans[i] = count;
            bool flag = true;
            for (int j = 31; j >= 0; --j)
            {
                if (flag)
                {
                    flag = false;
                    bit[j]++;
                    if (bit[j] == 2)
                    {
                        bit[j] = 0;
                        flag = true;
                        --count;
                    }
                    else ++count;
                }
            }
        }
        return ans;
    }
}

//
public class Solution
{
    public int[] CountBits(int num)
    {
        int[] counts = new int[num + 1];
        for (int i = 1; i < counts.Length; i++)
        {
            counts[i] = counts[i / 2] + (i % 2);
        }
        return counts;
    }
}