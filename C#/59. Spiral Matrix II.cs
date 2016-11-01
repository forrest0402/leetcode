public class Solution
{
    public int[,] GenerateMatrix(int n)
    {
        int[,] matrix = new int[n, n];
        if (n == 1)
            matrix[0, 0] = 1;
        int layer = 0, count = 0, maxL = (int)Math.Ceiling(n / 2.0);
        while (layer < maxL)
        {
            int row = layer, col = layer;
            matrix[row, col] = ++count;
            for (int i = 1; i < n - 1 - layer * 2; ++i)
                matrix[row, col + i] = ++count;
            for (int i = 0; i < n - 1 - layer * 2; ++i)
                matrix[row + i, col + n - 1 - layer * 2] = ++count;
            for (int i = 0; i < n - 1 - layer * 2; ++i)
                matrix[row + n - 1 - layer * 2, col + n - 1 - layer * 2 - i] = ++count;
            for (int i = 0; i < n - 1 - layer * 2; ++i)
                matrix[row + n - 1 - layer * 2 - i, col] = ++count;
            ++layer;
        }
        return matrix;
    }
}