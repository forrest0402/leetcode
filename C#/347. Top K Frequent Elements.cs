public class Solution
{
    public IList<int> TopKFrequent(int[] nums, int k)
    {
        if (nums == null)
            return null;
        Dictionary<int, int> dic = new Dictionary<int, int>();
        int count = 1;
        for (int i = 0; i < nums.Length; ++i)
        {
            if (dic.ContainsKey(nums[i]))
            {
                dic[nums[i]]++;
                if (dic[nums[i]] > count)
                    count = dic[nums[i]];
            }
            else
                dic.Add(nums[i], 1);
        }
        List<int> ans = new List<int>();
        List<int>[] sort = new List<int>[count + 1];
        foreach (int key in dic.Keys)
        {
            if (sort[dic[key]] == null)
                sort[dic[key]] = new List<int>();
            sort[dic[key]].Add(key);
        }
        for (int i = count; i >= 0 && k > 0; --i)
        {
            if (sort[i] != null)
            {
                ans.AddRange(sort[i]);
                k -= sort[i].Count;
            }
        }
        return ans;
    }
}

//More fast
public class Solution
{
    public IList<int> TopKFrequent(int[] nums, int k)
    {
        if (nums == null)
            return null;
        Dictionary<int, int> dic = new Dictionary<int, int>();
        int count = 1;
        for (int i = 0; i < nums.Length; ++i)
        {
            if (dic.ContainsKey(nums[i]))
            {
                dic[nums[i]]++;
                if (dic[nums[i]] > count)
                    count = dic[nums[i]];
            }
            else
                dic.Add(nums[i], 1);
        }
        IList<int> ans = new List<int>();
        string[] sort = new string[count + 1];
        foreach (int key in dic.Keys)
        {
            if (sort[dic[key]] == null)
                sort[dic[key]] = key.ToString();
            else sort[dic[key]] += "$" + key;
        }
        for (int i = count; i >= 0 && k > 0; --i)
        {
            if (sort[i] != null)
            {
                foreach (string str in sort[i].Split('$'))
                {
                    ans.Add(int.Parse(str));
                    --k;
                }
            }
        }
        return ans;
    }
}
