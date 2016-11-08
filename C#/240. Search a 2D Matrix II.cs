public class Solution
{
    public bool SearchMatrix(int[,] matrix, int target)
    {
        int row = 0, col = matrix.GetLength(1) - 1, len = matrix.GetLength(0);
        while (row < len && col >= 0)
        {
            if (matrix[row, col] == target) return true;
            if (matrix[row, col] > target) --col;
            else ++row;
        }
        return false;
    }
}