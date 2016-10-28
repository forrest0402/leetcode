public class Solution
{
    public int MaxSubArray(int[] nums)
    {
        int sum = 0, maxsum = nums[0];
        for (int i = 0; i < nums.Length; ++i)
        {
            sum = Math.Max(sum + nums[i], nums[i]);
            if (sum > maxsum)
                maxsum = sum;
        }
        return maxsum;
    }
}