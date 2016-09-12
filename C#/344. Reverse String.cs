public class Solution
{
    public string ReverseString(string s)
    {
        char[] charArray = s.ToCharArray();
        int lPos = -1, rPos = s.Length;
        while (++lPos < --rPos)
        {
            char tempC = charArray[lPos];
            charArray[lPos] = charArray[rPos];
            charArray[rPos] = tempC;
        }
        return new string(charArray);
    }
}