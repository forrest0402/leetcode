# LeetCode 
[LeetCode OJ]
## 344. Reverse String
>When to change a string, use toCharArray() method and use new string() to convert char[] to string back. Do not build a new string and add chars to it continuously because it is inefficient.

[Reverse String] - 20160912

## 371. Sum of Two Integers
>We can use xor to simulate addition. And use add and shifting to position carry.

[Sum of Two Integers] - 20160913

## 231. Power of Two
>There are errors with Math.Log(n, base)  
>e.g. Math.Log(536870912, 2) = 29.000000000000004 (expected 29)  
    
    if (n == 0)
      return false;
    double ans = Math.Log(n, 2);
    return Math.Min(ans - Math.Floor(ans), Math.Ceiling(ans) - ans) < 1e-10;

[Power of Two] - 20160914

## 374. Guess Number Higher or Lower
>It's okay to substitute (low+high)>>1 for (low+high)/2 because it is more efficient, however, we still face the problem that low+high could be larger than int.MaxValue. In this case, we can substitute >>> for >>.  
>Another solution is to use low+(high-low)/2.


    int low = 1, high = n;
    while (low <= high)
    {
        int number = (low + high) >>> 1;
        int ans = guess(number);
        if (ans == 0)
            return number;
        if (ans == -1)
            high = number - 1;
        else low = number + 1;
    }

[Guess Number Higher or Lower] - 20160919

[LeetCode OJ]:https://leetcode.com/
[Reverse String]: https://leetcode.com/problems/reverse-string/
[Sum of Two Integers]:https://leetcode.com/problems/sum-of-two-integers/
[Power of Two]:https://leetcode.com/problems/power-of-two/
[Guess Number Higher or Lower]:https://leetcode.com/problems/guess-number-higher-or-lower/