public class Solution
{
    public int RemoveElement(int[] nums, int val)
    {
        List<int> array = new List<int>();
        foreach (int i in nums)
            if (i != val)
                array.Add(i);
        for (int i = 0; i < array.Count; ++i)
            nums[i] = array[i];
        return array.Count;
    }
}