/* The isBadVersion API is defined in the parent class VersionControl.
      bool IsBadVersion(int version); */

public class Solution : VersionControl
{
    public int FirstBadVersion(int n)
    {
        if (n == 0)
            return 0;
        int low = 1, high = n;
        while (low < high)
        {
            int mid = low + (high - low) / 2;
            if (IsBadVersion(mid))
                high = mid - 1;
            else
                low = mid + 1;
        }
        if (IsBadVersion(low))
            return low;
        return low + 1;
    }
}