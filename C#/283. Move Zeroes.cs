public class Solution
{
    public void MoveZeroes(int[] nums)
    {
        int start = 0;
        for (int i = 0; i < nums.Length; ++i)
            if (nums[i] != 0)
                nums[start++] = nums[i];
        for (int i = start; i < nums.Length; ++i)
            nums[i] = 0;
    }
}