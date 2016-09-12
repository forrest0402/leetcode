public class Solution
{
    public string ReverseString(string s)
    {
        char[] charArray = s.ToCharArray();
        int lPos = 0, rPos = s.Length - 1;
        while (lPos < rPos)
        {
            char tempC = charArray[lPos];
            charArray[lPos] = charArray[rPos];
            charArray[rPos] = tempC;
            ++lPos;
            --rPos;
        }
        return new string(charArray);
    }
}