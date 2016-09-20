public class Solution
{
    public void Merge(int[] nums1, int m, int[] nums2, int n)
    {
        int[] list = new int[m + n];
        int p1 = 0, p2 = 0, count = 0;
        while (p1 < m && p2 < n)
        {
            if (nums1[p1] < nums2[p2])
                list[count++] = nums1[p1++];
            else if (nums1[p1] > nums2[p2])
                list[count++] = nums2[p2++];
            else
            {
                list[count++] = nums1[p1++];
                list[count++] = nums2[p2++];
            }
        }
        for (int i = p1; i < m; ++i)
            list[count++] = nums1[i];
        for (int i = p2; i < n; ++i)
            list[count++] = nums2[i];
        for (int i = 0; i < count; ++i)
            nums1[i] = list[i];
    }
}