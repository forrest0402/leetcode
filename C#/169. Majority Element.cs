public class Solution
{
    public int MajorityElement(int[] nums)
    {
        Dictionary<int, int> dic = new Dictionary<int, int>();
        foreach (int i in nums)
        {
            if (dic.ContainsKey(i))
                dic[i]++;
            else dic.Add(i, 1);
        }
        int num = 0, element = 0;
        foreach (int key in dic.Keys)
        {
            if (dic[key] > num)
            {
                num = dic[key];
                element = key;
            }
        }
        return element;
    }
}