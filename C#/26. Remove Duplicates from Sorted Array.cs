public class Solution
{
    public int RemoveDuplicates(int[] nums)
    {
        if (nums.Length <= 1)
            return nums.Length;
        int slow = 0, fast = 1;
        while (fast < nums.Length)
        {
            if (nums[fast] == nums[slow])
                ++fast;
            else
                nums[++slow] = nums[fast++];
        }
        return slow + 1;
    }
}