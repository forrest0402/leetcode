public class Solution
{
    public bool IsValidSudoku(char[,] board)
    {
        for (int i = 0; i < 9; ++i)
        {
            bool[] rowVisited = new bool[10];
            bool[] colVisited = new bool[10];
            for (int j = 0; j < 9; ++j)
            {
                if (board[i, j] != '.')
                {
                    if (rowVisited[board[i, j] - '0'])
                        return false;
                    rowVisited[board[i, j] - '0'] = true;
                }
                if (board[j, i] != '.')
                {
                    if (colVisited[board[j, i] - '0'])
                        return false;
                    colVisited[board[j, i] - '0'] = true;
                }
            }
        }
        for (int i = 0; i < 9; i += 3)
        {
            for (int j = 0; j < 9; j += 3)
            {
                bool[] visited = new bool[10];
                for (int k1 = 0; k1 < 3; ++k1)
                {
                    for (int k2 = 0; k2 < 3; ++k2)
                    {
                        if (board[i + k1, j + k2] != '.')
                        {
                            if (visited[board[i + k1, j + k2] - '0'])
                                return false;
                            visited[board[i + k1, j + k2] - '0'] = true;
                        }
                    }
                }
            }
        }
        return true;
    }
}