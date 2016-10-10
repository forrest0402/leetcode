public class Solution
{
    public int SingleNumber(int[] nums)
    {
        int[] bit = new int[32];
        int ans = 0;
        for (int b = 0; b < 32; ++b)
        {
            foreach (int i in nums)
                bit[b] += (i >> b) & 1;
            ans |= (bit[b] % 3) << b;
        }
        return ans;
    }
}