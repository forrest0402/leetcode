public class Solution
{
    public void Rotate(int[] nums, int k)
    {
        if (nums == null || nums.Length == 0 || k == 0)
            return;
        int n1 = nums[0], curN = n1, pos = 0, count = 0;
        bool first = true;
        HashSet<int> visited = new HashSet<int>();
        while (count < nums.Length)
        {
            while (visited.Contains(pos))
            {
                pos = (pos + 1) % nums.Length;
                curN = nums[pos];
            }
            visited.Add(pos);
            int rPos = (pos + k) % nums.Length;
            int temp = nums[rPos];
            nums[rPos] = curN;
            curN = temp;
            pos = rPos;
            ++count;
        }
    }
}