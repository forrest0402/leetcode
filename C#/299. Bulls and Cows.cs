public class Solution
{
    public string GetHint(string secret, string guess)
    {
        bool[] charg = new bool[secret.Length];
        bool[] chars = new bool[secret.Length];
        int A = 0, B = 0;
        for (int i = 0; i < guess.Length; ++i)
        {
            if (secret[i] == guess[i])
            {
                chars[i] = true;
                charg[i] = true;
                ++A;
            }
        }
        for (int i = 0; i < guess.Length; ++i)
        {
            if (chars[i])
                continue;
            int index = -1;
            for (int j = 0; j < secret.Length; ++j)
            {
                if (charg[j])
                    continue;
                if (secret[j] == guess[i])
                    index = j;
            }
            if (index >= 0 && !charg[index])
            {
                charg[index] = true;
                if (index == i)
                    ++A;
                else ++B;
            }
        }
        return A + "A" + B + "B";
    }
}