public class Solution
{
    public string AddBinary(string a, string b)
    {
        while (a.Length > 1 && a[0] == '0')
            a = a.Remove(0, 1);
        while (b.Length > 1 && b[0] == '0')
            b = b.Remove(0, 1);
        if (a == "")
            return b;
        if (b == "")
            return a;
        int len = a.Length > b.Length ? a.Length : b.Length;
        a = a.PadLeft(len, '0');
        b = b.PadLeft(len, '0');
        int flag = 0;
        char[] array = new char[len];
        for (int i = len - 1; i >= 0; --i)
        {
            int bit = int.Parse(a[i] + "") + int.Parse(b[i] + "") + flag;
            if (bit == 0 || bit == 1)
            {
                array[i] = Convert.ToChar(bit + '0');
                flag = 0;
            }
            else if (bit == 2)
            {
                array[i] = '0';
                flag = 1;
            }
            else
            {
                array[i] = '1';
                flag = 1;
            }
        }
        string ans = new string(array);
        if (flag == 1)
            ans = "1" + ans;
        return ans;
    }
}