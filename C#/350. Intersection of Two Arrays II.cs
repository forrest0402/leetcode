public class Solution
{
    public int[] Intersect(int[] nums1, int[] nums2)
    {
        Dictionary<int, int> dic1 = new Dictionary<int, int>();
        Dictionary<int, int> dic2 = new Dictionary<int, int>();
        foreach (int i in nums1)
        {
            if (dic1.ContainsKey(i))
                dic1[i]++;
            else dic1.Add(i, 1);
        }
        int count = 0, index = 0;
        foreach (int i in nums2)
        {
            if (dic1.ContainsKey(i))
            {
                ++count;
                if (dic2.ContainsKey(i))
                    dic2[i]++;
                else dic2.Add(i, 1);
                dic1[i]--;
                if (dic1[i] == 0)
                    dic1.Remove(i);
            }
        }
        int[] array = new int[count];
        foreach (int key in dic2.Keys)
        {
            for (int i = 0; i < dic2[key]; ++i)
                array[index++] = key;
        }
        return array;
    }
}