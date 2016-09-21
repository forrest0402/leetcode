public class Solution
{
    public int MaxRotateFunction(int[] A)
    {
        if (A.Length == 0)
            return 0;
        int pre = 0, num = 0;
        for (int i = 0; i < A.Length; ++i)
        {
            pre += A[i] * i;
            num += A[i];
        }
        int maxValue = pre;
        for (int i = 1; i < A.Length; ++i)
        {
            pre += num - A.Length * A[A.Length - i];
            if (pre > maxValue)
                maxValue = pre;
        }
        return maxValue;
    }
}