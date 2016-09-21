public class Solution
{
    public int[] TwoSum(int[] nums, int target)
    {
        if (nums == null || nums.Length < 2)
            return new int[2];
        int[] ans = new int[2];
        for (int i = 0; i < nums.Length; ++i)
        {
            for (int j = nums.Length - 1; j > i; --j)
            {
                if (nums[i] + nums[j] == target)
                {
                    ans[0] = i;
                    ans[1] = j;
                }
            }
        }
        return ans;
    }
}