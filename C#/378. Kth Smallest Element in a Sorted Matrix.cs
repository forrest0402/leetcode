public class Solution
{
    public int KthSmallest(int[,] matrix, int k)
    {
        int row = matrix.GetLength(0);
        int col = matrix.GetLength(1);
        SortedList<int, Tuple<int, int>> queue = new SortedList<int, Tuple<int, int>>(new DuplicateKeyComparer<int>());
        queue.Add(matrix[0, 0], new Tuple<int, int>(0, 0));
        bool[,] visited = new bool[row, col];
        while (queue.Count > 0)
        {
            Tuple<int, int> node = queue.ElementAt(0).Value;
            if (--k == 0)
                return queue.ElementAt(0).Key;
            queue.RemoveAt(0);
            if (node.Item1 + 1 < row && !visited[node.Item1 + 1, node.Item2])
            {
                queue.Add(matrix[node.Item1 + 1, node.Item2], new Tuple<int, int>(node.Item1 + 1, node.Item2));
                visited[node.Item1 + 1, node.Item2] = true;
            }
            if (node.Item2 + 1 < col && !visited[node.Item1, node.Item2 + 1])
            {
                queue.Add(matrix[node.Item1, node.Item2 + 1], new Tuple<int, int>(node.Item1, node.Item2 + 1));
                visited[node.Item1, node.Item2 + 1] = true;
            }
        }
        return -1;
    }
}
/// <summary>
/// Comparer for comparing two keys, handling equality as beeing greater
/// Use this Comparer e.g. with SortedLists or SortedDictionaries, that don't allow duplicate keys
/// </summary>
/// <typeparam name="TKey"></typeparam>
public class DuplicateKeyComparer<TKey> : IComparer<TKey> where TKey : IComparable
{
    public int Compare(TKey x, TKey y)
    {
        int result = x.CompareTo(y);
        if (result == 0)
            return 1;   // Handle equality as beeing greater
        else
            return result;
    }
}




//
public class Solution
{
    public int KthSmallest(int[,] matrix, int k)
    {
        int row = matrix.GetLength(0);
        int col = matrix.GetLength(1);
        int count = 0;
        int[] array = new int[matrix.Length];
        for (int i = 0; i < row; ++i)
        {
            for (int j = 0; j < col; ++j)
            {
                array[count++] = matrix[i, j];
            }
        }
        Array.Sort(array);
        return array[k - 1];
    }
}

