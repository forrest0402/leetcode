public class Solution
{
    public long TenPow(int n)
    {
        long ans = 1;
        while (n-- > 0)
        {
            ans *= 10;
        }
        return ans;
    }
    public int MyAtoi(string str)
    {
        bool flag = false;
        if (str == "")
            return 0;
        for (int i = 0; i < str.Length; ++i)
        {
            if (str[i] == ' ')
                str = str.Remove(i--, 1);
            else break;
        }
        if (str == "")
            return 0;
        if (str[0] == '+')
            str = str.Remove(0, 1);
        else if (str[0] == '-')
        {
            flag = true;
            str = str.Remove(0, 1);
        }
        if (str == "")
            return 0;
        int count = 0, length = -1;
        long ans = 0;
        for (int i = 0; i < str.Length; ++i)
        {
            if (str[i] >= '0' && str[i] <= '9')
            {
                length = i;
            }
            else
            {
                if (length == -1)
                    return 0;
                else break;
            }
        }
        for (int i = length; i >= 0; --i)
        {
            ans += TenPow(count++) * (str[i] - '0');
            long temp = flag ? -ans : ans;
            if (temp > int.MaxValue)
                return int.MaxValue;
            if (temp < int.MinValue)
                return int.MinValue;
        }
        if (flag)
            ans = -ans;
        if (ans > int.MaxValue)
            return int.MaxValue;
        if (ans < int.MinValue)
            return int.MinValue;
        return (int)ans;
    }
}