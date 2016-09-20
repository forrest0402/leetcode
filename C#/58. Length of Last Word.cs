public class Solution
{
    public int LengthOfLastWord(string s)
    {
        if (s == "")
            return 0;
        string[] array = s.Trim(' ').Split(' ');
        return array[array.Length - 1].Length;
    }
}