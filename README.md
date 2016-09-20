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

## 160. Intersection of Two Linked Lists
>[Floyd Cycle Detection Algorithm] is a pointer algorithm that uses only two pointers, which move through the sequence at different speeds. It is also called the "tortoise and the hare algorithm", alluding to Aesop's fable of The Tortoise and the Hare.

![Alt text](/image/cycledetection2.png)

Assume we have two pointers *t* (tortoise) and *h* (hare), when *t* and *h* encouter (C is the length of the circle, M is the node where *t* and *h* encounter) :  
step\_t = p + m + a \* C   
step\_h = 2 \* step\_t = p + m + b \* C  
step\_h - step\_t = step\_t = (b - a) * C = p + m + a * C  
Then we can calculate:  
1. The length of the circle: let *t* move forward until it reaches M again. This time, the steps of *t* equal the length of the circle.  
2. Start position of the circle: let *t* returns S. And let both *t* and *h* move forward at one step per time. Finally, they will meet each other at P.


    public ListNode GetIntersectionNode(ListNode headA, ListNode headB)
    {
        ListNode a = headA, b = headB;
        if (a == null || b == null)
            return null;
        while (a != b)
        {
            a = a == null ? headB : a.next;
            b = b == null ? headA : b.next;
        }
        return a;
    }

[Intersection of Two Linked Lists] - 20160920



[LeetCode OJ]:https://leetcode.com/
[Reverse String]: https://leetcode.com/problems/reverse-string/
[Sum of Two Integers]:https://leetcode.com/problems/sum-of-two-integers/
[Power of Two]:https://leetcode.com/problems/power-of-two/
[Guess Number Higher or Lower]:https://leetcode.com/problems/guess-number-higher-or-lower/
[Intersection of Two Linked Lists]:https://leetcode.com/problems/intersection-of-two-linked-lists/
[Floyd Cycle Detection Algorithm]:https://en.wikipedia.org/wiki/Cycle_detection
