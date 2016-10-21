public class Solution
{
    public string OriginalDigits(string s)
    {
        StringBuilder ans = new StringBuilder();
        int x0 = 0, x1 = 0, x2 = 0, x3 = 0, x4 = 0, x5 = 0, x6 = 0, x7 = 0, x8 = 0, x9 = 0, vv = 0, vo = 0, vh = 0, vs = 0, vi = 0;
        foreach (char chs in s)
        {
            if (chs == 'z') ++x0;
            else if (chs == 'o') ++vo;
            else if (chs == 'w') ++x2;
            else if (chs == 'h') ++vh;
            else if (chs == 'u') ++x4;
            else if (chs == 'v') ++vv;
            else if (chs == 'x') ++x6;
            else if (chs == 's') ++vs;
            else if (chs == 'g') ++x8;
            else if (chs == 'i') ++vi;
        }
        x1 = vo - x0 - x2 - x4;
        x3 = vh - x8;
        x7 = vs - x6;
        x5 = vv - x7;
        x9 = vi - x8 - x6 - x5;
        while (x0-- > 0) ans.Append('0');
        while (x1-- > 0) ans.Append('1');
        while (x2-- > 0) ans.Append('2');
        while (x3-- > 0) ans.Append('3');
        while (x4-- > 0) ans.Append('4');
        while (x5-- > 0) ans.Append('5');
        while (x6-- > 0) ans.Append('6');
        while (x7-- > 0) ans.Append('7');
        while (x8-- > 0) ans.Append('8');
        while (x9-- > 0) ans.Append('9');
        return ans.ToString();
    }
}