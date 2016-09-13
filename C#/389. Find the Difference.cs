public class Solution
{
    public char FindTheDifference(string s, string t)
    {
        int[] array = new int[123];
        foreach (char ch in s)
            array[(int)ch]++;
        foreach (char ch in t)
            array[(int)ch]--;
        for (int i = 0; i < 123; ++i)
            if (array[i] < 0)
                return (char)i;
        return 'a';
    }
}