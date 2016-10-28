public class Solution
{
    public int FindMin(int[] nums)
    {
        int l = 0, r = nums.Length - 1, mid = 0, ans = nums[0];
        while (l <= r)
        {
            if (l == r)
            {
                ans = nums[l];
                break;
            }
            if (nums[l] < nums[r])
            {
                ans = nums[l];
                break;
            }
            mid = l + (r - l) / 2;
            if (nums[l] <= nums[mid])
                ++l;
            else r = mid;
        }
        return ans;
    }
}


public class Solution
{
    public int FindMin(int[] nums)
    {
        Array.Sort(nums);
        return nums[0];
    }
}