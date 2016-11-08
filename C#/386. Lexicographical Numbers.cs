public class Solution
{
    List<int> ans = new List<int>();
    void AddNum(int num, int n, int addN)
    {
        if (num + addN <= n)
            ans.Add(num + addN);
        else return;
        AddNum((num + addN) * 10, n, 0);
        if ((num == 1 && addN <= 7) || (num > 1 && addN <= 8))
            AddNum(num, n, addN + 1);
    }
    public IList<int> LexicalOrder(int n)
    {
        AddNum(1, n, 0);
        return ans;
    }
}