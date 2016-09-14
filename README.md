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

[LeetCode OJ]:https://leetcode.com/
[Reverse String]: https://leetcode.com/problems/reverse-string/
[Sum of Two Integers]:https://leetcode.com/problems/sum-of-two-integers/
[Power of Two]:https://leetcode.com/problems/power-of-two/