public class Solution {
    public int IntegerBreak(int n) {
        if(n == 1 || n == 2)
            return 1;
        if(n == 3)
            return 2;
        int count = 1;
        while(n > 4){
            n -= 3;
            count *= 3;
        }
        return count * n;
    }
}