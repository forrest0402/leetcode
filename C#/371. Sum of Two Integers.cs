// basic idea - summator
public class Solution
{
    public int GetSum(int a, int b)
    {
        string n1 = Convert.ToString(a, 2).PadLeft(32, '0');
        string n2 = Convert.ToString(b, 2).PadLeft(32, '0');
        string ans = "";
        int flag = 0;
        for (int i = 31; i >= 0; --i)
        {
            ans = (((int)n1[i]) ^ ((int)n2[i]) ^ flag) + ans;
            if ((n1[i] == '1' && n2[i] == '1') || (n1[i] == '1' && flag == 1) || (flag == 1 && n2[i] == '1'))
                flag = 1;
            else flag = 0;
        }
        return Convert.ToInt32(ans, 2);
    }
}

// bit operation - version 1
public class Solution
{
    public int GetSum(int a, int b)
    {
        int sum = 0;
        while (b != 0)
        {
            sum = a ^ b;
            b = (a & b) << 1;
            a = sum;
        }
        return sum;
    }
}

// bit operation - version 2
public class Solution
{
    public int GetSum(int a, int b)
    {
        return b == 0 ? a : GetSum(a ^ b, (a & b) << 1);
    }
}
