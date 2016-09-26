public class Solution
{
    public int[] ProductExceptSelf(int[] nums)
    {
        int n = 1;
        int flag = 0;
        foreach (int i in nums)
        {
            if (i != 0)
                n *= i;
            else flag++;
        }
        for (int i = 0; i < nums.Length; ++i)
        {
            if (flag == 0)
                nums[i] = n / nums[i];
            else if (flag == 1)
                nums[i] = nums[i] == 0 ? n : 0;
            else nums[i] = 0;
        }
        return nums;
    }
}

//
public class Solution
{
    public int[] ProductExceptSelf(int[] nums)
    {
        if (nums == null || nums.Length == 1)
            return nums;
        int n = 1;
        int[] ans = new int[nums.Length];
        for (int i = 0; i < nums.Length; ++i)
        {
            ans[i] = n;
            n *= nums[i];
        }
        n = 1;
        for (int i = nums.Length - 1; i >= 0; --i)
        {
            ans[i] *= n;
            n *= nums[i];
        }
        return ans;
    }
}
//

