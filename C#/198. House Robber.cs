public class Solution
{
    public int Rob(int[] nums)
    {
        if (nums.Length == 0)
            return 0;
        if (nums.Length == 1)
            return nums[0];
        if (nums.Length == 2)
            return nums[0] > nums[1] ? nums[0] : nums[1];
        int[] array = new int[nums.Length];
        array[0] = nums[0];
        array[1] = nums[1] > nums[0] ? nums[1] : nums[0];
        for (int i = 2; i < nums.Length; ++i)
            array[i] = array[i - 1] >= array[i - 2] + nums[i] ? array[i - 1] : array[i - 2] + nums[i];
        return array[nums.Length - 1];
    }
}