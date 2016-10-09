public class Solution
{
    List<int> DFS(string exp)
    {
        bool flag = true;
        int index = -1;
        List<int> ans = new List<int>();
        while (flag)
        {
            flag = false;
            for (int i = index + 1; i < exp.Length; ++i)
            {
                if (exp[i] == '*' || exp[i] == '+' || exp[i] == '-')
                {
                    index = i;
                    flag = true;
                    break;
                }
            }
            if (!flag)
            {
                if (index == -1)
                    return new List<int>() { int.Parse(exp) };
                else break;
            }
            string ls = exp.Substring(0, index), rs = exp.Substring(index + 1);
            foreach (int i in DFS(ls))
            {
                foreach (int j in DFS(rs))
                {
                    if (exp[index] == '*')
                        ans.Add(j * i);
                    else if (exp[index] == '+')
                        ans.Add(j + i);
                    else if (exp[index] == '-')
                        ans.Add(i - j);
                }
            }
        }
        return ans;
    }
    public IList<int> DiffWaysToCompute(string input)
    {
        return DFS(input);
    }
}