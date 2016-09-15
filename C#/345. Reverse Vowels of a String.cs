public class Solution
{
    public bool isVowel(char chs)
    {
        if (chs == 'a' || chs == 'e' || chs == 'i' || chs == 'o' || chs == 'u' || chs == 'A' || chs == 'E' || chs == 'I' || chs == 'O' || chs == 'U')
            return true;
        return false;
    }
    public string ReverseVowels(string s)
    {
        char[] array = s.ToCharArray();
        int lPos = 0, rPos = s.Length - 1;
        bool flag = false;
        while (lPos < rPos)
        {
            if (isVowel(s[lPos]) && isVowel(s[rPos]))
                flag = true;
            else flag = false;
            if (flag)
            {
                char chs = array[lPos];
                array[lPos] = array[rPos];
                array[rPos] = chs;
                ++lPos;
                --rPos;
            }
            else
            {
                while (lPos < s.Length && !isVowel(s[lPos]))
                    ++lPos;
                while (rPos >= 0 && !isVowel(s[rPos]))
                    --rPos;
            }
        }
        return new string(array);
    }
}