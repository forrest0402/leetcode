public class Solution
{
    private List<IList<int>> DFS(List<int> list)
    {
        List<IList<int>> ans = new List<IList<int>>();
        if (list.Count == 1)
        {
            ans.Add(new List<int>() { list[0] });
            return ans;
        }
        int n = list[0];
        list.RemoveAt(0);
        List<IList<int>> allPer = DFS(list);
        foreach (IList<int> p in allPer)
        {
            for (int i = 0; i <= p.Count; ++i)
            {
                List<int> newP = new List<int>(p);
                newP.Insert(i, n);
                ans.Add(newP);
            }
        }
        return ans;
    }
    public IList<IList<int>> Permute(int[] nums)
    {
        return DFS(nums.ToList());
    }
}