public class Solution
{
    List<IList<int>> ans = null;
    bool[] visited = null;
    private void DFS(int k, int n, int cn, int pre)
    {
        if (k == 0)
        {
            if (cn == n)
            {
                IList<int> solu = new List<int>();
                for (int i = 1; i < 10; ++i)
                    if (visited[i])
                        solu.Add(i);
                ans.Add(solu);
            }
            return;
        }
        if (cn >= n)
            return;
        for (int i = pre; i < 10; ++i)
        {
            if (visited[i])
                continue;
            visited[i] = true;
            DFS(k - 1, n, cn + i, i);
            visited[i] = false;
        }
    }
    public IList<IList<int>> CombinationSum3(int k, int n)
    {
        ans = new List<IList<int>>();
        visited = new bool[10];
        DFS(k, n, 0, 1);
        return ans;
    }
}