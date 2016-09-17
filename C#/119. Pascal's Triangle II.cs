//
public class Solution
{
    public IList<int> GetRow(int rowIndex)
    {
        ++rowIndex;
        List<IList<int>> ans = new List<IList<int>>();
        int numRows = rowIndex;
        for (int i = 1; i <= numRows; ++i)
        {
            if (i == 1)
                ans.Add(new List<int>() { 1 });
            else
            {
                int[] row = new int[i];
                row[0] = row[i - 1] = 1;
                for (int j = 1; j < i - 1; ++j)
                    row[j] = ans[i - 2][j - 1] + ans[i - 2][j];
                ans.Add(row.ToList());
            }
        }
        return ans[rowIndex - 1];
    }
}
// O(k) space algorithm, use an array to store one row because each row only depends on above row 
