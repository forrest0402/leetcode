public class Solution
{
    public int[] PlusOne(int[] digits)
    {
        if (digits == null)
            return null;
        if (digits.Length == 0)
            return digits;
        bool flag = false;
        int carry = 10;
        digits[digits.Length - 1]++;
        for (int i = digits.Length - 1; i >= 0; --i)
        {
            if (flag)
                digits[i]++;
            if (digits[i] >= carry)
            {
                flag = true;
                digits[i] -= carry;
            }
            else
            {
                flag = false;
                break;
            }
        }
        if (!flag)
            return digits;
        else
        {
            List<int> tempList = digits.ToList();
            tempList.Insert(0, 1);
            return tempList.ToArray();
        }
    }
}