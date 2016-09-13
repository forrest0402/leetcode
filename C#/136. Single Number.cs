public class Solution
{
    public int SingleNumber(int[] nums)
    {
        int ans = 0;
        foreach (int i in nums)
            ans ^= i;
        return ans;
    }
}