public class Solution
{
    public int[] SingleNumber(int[] nums)
    {
        if (nums == null || nums.Length < 2)
            return new int[] { 0, 0 };
        HashSet<int> set = new HashSet<int>();
        foreach (int i in nums)
        {
            if (!set.Contains(i))
                set.Add(i);
            else set.Remove(i);
        }
        return set.ToArray();
    }
}