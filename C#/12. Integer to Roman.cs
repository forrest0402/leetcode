public class Solution {
    public string IntToRoman(int num) {
        string[] symbol = { "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" };
        int[] value = { 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 };
        int index = 0;
        string ans = "";
        while(num != 0){
            if(value[index] <= num){
                num -= value[index];
                ans += symbol[index];
            }
            else ++index;
        }
        return ans;
    }
}