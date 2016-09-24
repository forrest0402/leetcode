public class Solution
{
    public int[] TwoSum(int[] numbers, int target)
    {
        int index1 = 0, index2 = 0;
        for (int i = 0; i < numbers.Length - 1; ++i)
        {
            index1 = i;
            int l = index1 + 1, r = numbers.Length - 1, mid = 0, n = target - numbers[index1];
            while (l <= r)
            {
                mid = l + (r - l) / 2;
                if (numbers[mid] == n)
                    break;
                if (numbers[mid] > n)
                    r = mid - 1;
                else l = mid + 1;
            }
            if (numbers[mid] == n)
            {
                index2 = mid;
                break;
            }
        }
        return new int[] { index1 + 1, index2 + 1 };
    }
}