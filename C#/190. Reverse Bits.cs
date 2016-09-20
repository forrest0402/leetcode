public class Solution
{
    public uint reverseBits(uint n)
    {
        char[] arrays = Convert.ToString(n, 2).PadLeft(32, '0').ToCharArray();
        Array.Reverse(arrays);
        return Convert.ToUInt32(new string(arrays), 2);
    }
}