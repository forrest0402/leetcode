public class NumArray
{
    int[] sums = null;
    int[] myNums = null;
    public NumArray(int[] nums)
    {
        if (nums == null || nums.Length == 0)
            return;
        sums = new int[nums.Length];
        myNums = new int[nums.Length];
        sums[0] = myNums[0] = nums[0];
        for (int i = 1; i < nums.Length; ++i)
        {
            sums[i] = sums[i - 1] + nums[i];
            myNums[i] = nums[i];
        }
    }

    public int SumRange(int i, int j)
    {
        if (sums == null)
            return 0;
        i = i < 0 ? 0 : i;
        j = j > sums.Length - 1 ? sums.Length - 1 : j;
        return sums[j] - sums[i] + myNums[i];
    }
}


// Your NumArray object will be instantiated and called as such:
// NumArray numArray = new NumArray(nums);
// numArray.sumRange(0, 1);
// numArray.sumRange(1, 2);