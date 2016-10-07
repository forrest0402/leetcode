public class Solution
{
    List<string> parentheses = null;
    private void DFS(int l, int r, int ln, string p)
    {
        if (l == 0 && r == 0)
        {
            parentheses.Add(p);
            return;
        }
        if (l >= 1)
            DFS(l - 1, r, ln + 1, p + "(");
        if (r >= 1)
        {
            if (ln > 0)
                --ln;
            else return;
            DFS(l, r - 1, ln, p + ")");
        }
    }
    public IList<string> GenerateParenthesis(int n)
    {
        parentheses = new List<string>();
        DFS(n, n, 0, "");
        return parentheses;
    }
}