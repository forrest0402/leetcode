# LeetCode 
[LeetCode OJ]

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

## 190. Reverse Bits
>One should be familiar with the basic operations of string.

    public uint reverseBits(uint n)
    {
        char[] arrays = Convert.ToString(n, 2).PadLeft(32, '0').ToCharArray();
        Array.Reverse(arrays);
        return Convert.ToUInt32(new string(arrays), 2);
    }

[Reverse Bits] - 20160920

## 204. Count Primes
>[sieve of Eratosthenes] In mathematics, the sieve of Eratosthenes (Ancient Greek: κόσκινον Ἐρατοσθένους, kóskinon Eratosthénous), one of a number of prime number sieves, is a simple, ancient algorithm for finding all prime numbers up to any given limit. It does so by iteratively marking as composite (i.e., not prime) the multiples of each prime, starting with the multiples of 2.

    private static readonly int MaxN = 5000000;
    bool[] primes = new bool[MaxN];
    //version 1
    public void SieveOfEratosthenes_v1(int n)
    {
        primes[0] = primes[1] = false;
        primes[2] = true;
        for (int i = 3; i < n; i++)
            primes[i] = i % 2 == 0 ? false : true;
        for (int i = 3; i <= Math.Sqrt(n); i++)
            if (primes[i])
                for (int j = i * 2; j < n; j += i)
                    primes[j] = false;
    }
    //skip duplicate numbers
    public void SieveOfEratosthenes_v2(int n)
    {
        primes[0] = primes[1] = false;
        primes[2] = true;
        for (int i = 3; i < n; i++)
            primes[i] = i % 2 == 0 ? false : true;
        for (int i = 3; i <= Math.Sqrt(n); i++)
            if (primes[i])
                for (int j = i * i; j < n; j += 2*i)
                    primes[j] = false;
    }

> A more fast method

    bool[] isPrime = new bool[60000001];
    int[] primes = new int[60000001 >> 1];
    public void PrimeSieve(int n)
    {
        for (int i = 0; i < n; ++i)
    		isPrime[i] = true;
    	int index = 0;
    	for (int i = 2; i < n; ++i)
    	{
    		if (isPrime[i])
    			primes[index++] = i;
    		for (int j = 0; j < index; ++j)
    		{
    			if (primes[j] * i > n)
    				break;
    			isPrime[primes[j] * i] = false;
    			if (i % primes[j] == 0)
    				break;
    		}
    	}
    }

>For the most fast method, see [Implementation of the Sieve of Atkin]. It is ten times faster than the above algorithms.

[Count Primes] - 20160922

## 231. Power of Two
>There are errors with Math.Log(n, base)  
>e.g. Math.Log(536870912, 2) = 29.000000000000004 (expected 29)  
    
    if (n == 0)
      return false;
    double ans = Math.Log(n, 2);
    return Math.Min(ans - Math.Floor(ans), Math.Ceiling(ans) - ans) < 1e-10;

[Power of Two] - 20160914

## 344. Reverse String
>When to change a string, use toCharArray() method and use new string() to convert char[] to string back. Do not build a new string and add chars to it continuously because it is inefficient.

[Reverse String] - 20160912

## 371. Sum of Two Integers
>We can use xor to simulate addition. And use add and shifting to position carry.

[Sum of Two Integers] - 20160913



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
[Intersection of Two Linked Lists]:https://leetcode.com/problems/intersection-of-two-linked-lists/
[Floyd Cycle Detection Algorithm]:https://en.wikipedia.org/wiki/Cycle_detection
[Reverse Bits]:https://leetcode.com/problems/reverse-bits/
[Count Primes]:https://leetcode.com/problems/count-primes/
[sieve of Eratosthenes]:https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
[Implementation of the Sieve of Atkin]:http://stackoverflow.com/questions/1569127/c-implementation-of-the-sieve-of-atkin