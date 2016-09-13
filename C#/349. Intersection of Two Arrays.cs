public class Solution
{
    public int[] Intersection(int[] nums1, int[] nums2)
    {
        HashSet<int> set1 = new HashSet<int>();
        HashSet<int> set2 = new HashSet<int>();
        foreach (int i in nums1)
            set1.Add(i);
        foreach (int i in nums2)
            if (set1.Contains(i))
                set2.Add(i);
        return set2.ToArray();
    }
}