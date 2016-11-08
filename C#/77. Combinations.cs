public class Solution
{
    public IList<IList<int>> AllCombinations(int start, int end, int k)
    {
        IList<IList<int>> ans = new List<IList<int>>();
        if (k == 1)
        {
            for (int i = start; i <= end; ++i)
                ans.Add(new List<int> { i });
            return ans;
        }
        for (int i = start; i < end; ++i)
        {
            IList<IList<int>> temp = AllCombinations(i + 1, end, k - 1);
            foreach (IList<int> tuple in temp)
            {
                tuple.Insert(0, i);
            }
            ans.AddRange(temp);
        }
        return ans;
    }
    public IList<IList<int>> Combine(int n, int k)
    {
        IList<IList<int>> ans = new List<IList<int>>();
        if (k == 1)
        {
            for (int i = 1; i <= n; ++i)
                ans.Add(new List<int> { i });
            return ans;
        }
        for (int i = 1; i < n; ++i)
        {
            List<IList<int>> temp = AllCombinations(i + 1, n, k - 1);
            foreach (IList<int> tuple in temp)
            {
                tuple.Insert(0, i);
            }
            ans.AddRange(temp);
        }
        return ans;
    }
}