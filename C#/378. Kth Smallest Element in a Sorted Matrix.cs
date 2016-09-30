public class Solution
{
    public int KthSmallest(int[,] matrix, int k)
    {
        int row = matrix.GetLength(0);
        int col = matrix.GetLength(1);
        SortedList<int, Node> queue = new SortedList<int, Node>(new DuplicateKeyComparer<int>());
        queue.Add(matrix[0, 0], new Node() { i = 0, j = 0 });
        bool[,] visited = new bool[row, col];
        while (queue.Count > 0)
        {
            Node node = queue.ElementAt(0).Value;
            if (--k == 0)
                return queue.ElementAt(0).Key;
            queue.RemoveAt(0);
            if (node.i + 1 < row && !visited[node.i + 1, node.j])
            {
                queue.Add(matrix[node.i + 1, node.j], new Node() { i = node.i + 1, j = node.j });
                visited[node.i + 1, node.j] = true;
            }
            if (node.j + 1 < col && !visited[node.i, node.j + 1])
            {
                queue.Add(matrix[node.i, node.j + 1], new Node() { i = node.i, j = node.j + 1 });
                visited[node.i, node.j + 1] = true;
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
public class Node
{
    public int i;
    public int j;
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

