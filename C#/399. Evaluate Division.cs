public class Solution
{
    Dictionary<string, double> equDic = new Dictionary<string, double>();
    HashSet<string> alphabeta = new HashSet<string>();
    private double DFS(string a, string b, HashSet<string> visited)
    {
        if (equDic.ContainsKey(a + "-" + b))
            return equDic[a + "-" + b];
        if (visited.Contains(a + "-" + b))
            return -1;
        visited.Add(a + "-" + b);
        foreach (string key in equDic.Keys)
        {
            string n1 = key.Split('-')[0], n2 = key.Split('-')[1];
            if (n1 == a)
            {
                double temp = DFS(n2, b, visited);
                if (!equDic.ContainsKey(n2 + "-" + b))
                    equDic.Add(n2 + "-" + b, temp);
                if (temp != -1.0)
                    return equDic[key] * temp;
                else return temp;
            }
            else if (n2 == a)
            {
                double temp = DFS(b, n1, visited);
                if (!equDic.ContainsKey(b + "-" + n1))
                    equDic.Add(b + "-" + n1, temp);
                if (temp != -1.0)
                    return 1.0 / (equDic[key] * temp);
                else return temp;
            }
        }
        return -1.0;
    }
    public double[] CalcEquation(string[,] equations, double[] values, string[,] queries)
    {
        for (int i = 0; i < equations.GetLength(0); ++i)
        {
            equDic.Add(equations[i, 0] + "-" + equations[i, 1], values[i]);
            equDic.Add(equations[i, 1] + "-" + equations[i, 0], 1.0 / values[i]);
            alphabeta.Add(equations[i, 0]);
            alphabeta.Add(equations[i, 1]);
        }
        foreach (string a in alphabeta)
            equDic.Add(a + "-" + a, 1);
        foreach (string a in alphabeta)
            foreach (string b in alphabeta)
                if (a != b && !equDic.ContainsKey(a + "-" + b))
                {
                    double v = DFS(a, b, new HashSet<string>());
                    if (!equDic.ContainsKey(a + "-" + b))
                        equDic.Add(a + "-" + b, v);
                }
        double[] ans = new double[queries.GetLength(0)];
        for (int i = 0; i < queries.GetLength(0); ++i)
            if (equDic.ContainsKey(queries[i, 0] + "-" + queries[i, 1]))
                ans[i] = equDic[queries[i, 0] + "-" + queries[i, 1]];
            else ans[i] = -1.0;
        return ans;
    }
}