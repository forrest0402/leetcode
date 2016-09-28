public class Solution
{
    public int MissingNumber(int[] nums)
    {
        int sum = 0, maxN = 0;
        foreach (int i in nums)
        {
            if (i > maxN)
                maxN = i;
            sum ^= i;
        }
        if (maxN + 1 == nums.Length)
            return maxN + 1;
        for (int i = 0; i <= nums.Length; ++i)
            sum ^= i;
        return sum;
    }
}
//
public class Solution
{
    public int MissingNumber(int[] nums)
    {
        int sum = 0, ans = 0, maxN = 0;
        for (int i = 0; i <= nums.Length; ++i)
        {
            if (i < nums.Length)
            {
                sum ^= nums[i];
                if (nums[i] > maxN)
                    maxN = nums[i];
            }
            ans ^= i;
        }
        if (maxN + 1 == nums.Length)
            return maxN + 1;
        return sum ^ ans;
    }
}