/* The guess API is defined in the parent class GuessGame.
   @param num, your guess
   @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
      int guess(int num); */

// This is Java version
public class Solution extends GuessGame
{
    public int guessNumber(int n) {
        int low = 1, high = n, number = 1;
        while (low <= high)
        {
            number = (low + high) >>> 1;
            int ans = guess(number);
            if (ans == 0)
                return number;
            if (ans == -1)
                high = number - 1;
            else low = number + 1;
        }
        return -1;
    }
}