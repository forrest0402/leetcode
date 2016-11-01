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
>One can also see [Eratosthenes-Sundaram-Atkins-Sieve-Implementation] for a survey.

[Count Primes] - 20160922

## 231. Power of Two
>There are errors with Math.Log(n, base)  
>e.g. Math.Log(536870912, 2) = 29.000000000000004 (expected 29)  

    if (n == 0)
      return false;
    double ans = Math.Log(n, 2);
    return Math.Min(ans - Math.Floor(ans), Math.Ceiling(ans) - ans) < 1e-10;

[Power of Two] - 20160914

## 337. House Robber III
>Dynamic Programming: For an array of integers, a classic question is to find the max-sum without picking two adjacent numbers. Usually, we can use a dp[i]=max(dp[i-1], dp[i-2]+c[i]) to find the max-sum. This time, we got a binary tree, thus, we can use a two-dimension dp to finish the task.

```C#
public class Solution
{
    private const int NOROB = 0;
    private const int ROB = 1;
    private int[] DP(TreeNode root)
    {
        if (root == null)
            return new int[] { 0, 0 };
        int[] dpLeft = DP(root.left);
        int[] dpRight = DP(root.right);
        int robThis = dpLeft[NOROB] + dpRight[NOROB] + root.val;
        int noRobThis = Math.Max(dpLeft[ROB], dpLeft[NOROB]) +
            Math.Max(dpRight[ROB], dpRight[NOROB]);
        return new int[] { noRobThis, robThis };
    }
    public int Rob(TreeNode root)
    {
        int[] dp = DP(root);
        return Math.Max(dp[NOROB], dp[ROB]);
    }
}
```

[House Robber III] - 20161005

## 338. Counting Bits
>Dynamic Programming: the number of ones in counts[i] equals the number of ones in counts[i/2] because i/2 means shifting i right except that we don't know whether the last digit of i is 1.

    public int[] CountBits(int num)
    {
        int[] counts = new int[num+1];
        for(int i = 1; i < counts.Length; i++)
            counts[i] = counts[i/2] + (i % 2);
        return counts;
    }

[Counting Bits] - 20160924

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


## 377. Combination Sum IV
>Dynamic Programming: The solution is similar to [Climbing Stairs]. In [Climbing Stairs], we have n steps, and we can define dp[i]=dp[i-1]+dp[i-2]. This time, we can add any number from the given *nums*. Therefore, we subsitute nums[j] for 1 and 2 and define dp[i]=sum(dp[i-nums[j]]).

```C#
public int CombinationSum4(int[] nums, int target)
{
    int[] dp = new int[target + 1];
    dp[0] = 1;
    for (int i = 1; i <= target; ++i)
        for (int j = 0; j < nums.Length; ++j)
            if (i - nums[j] >= 0)
                dp[i] += dp[i - nums[j]];
    return dp[target];
}
```
[Combination Sum IV] - 20161006

## 378. Kth Smallest Element in a Sorted Matrix
>BFS + PriorityQueue  
Notice the usage of SortedList and Tuple.

```
public class Solution
{
    public int KthSmallest(int[,] matrix, int k)
    {
        int row = matrix.GetLength(0);
        int col = matrix.GetLength(1);
        SortedList<int, Tuple<int, int>> queue = new SortedList<int, Tuple<int, int>>(new DuplicateKeyComparer<int>());
        queue.Add(matrix[0, 0], new Tuple<int, int>(0, 0));
        bool[,] visited = new bool[row, col];
        while (queue.Count > 0)
        {
            Tuple<int, int> node = queue.ElementAt(0).Value;
            if (--k == 0)
                return queue.ElementAt(0).Key;
            queue.RemoveAt(0);
            if (node.Item1 + 1 < row && !visited[node.Item1 + 1, node.Item2])
            {
                queue.Add(matrix[node.Item1 + 1, node.Item2], new Tuple<int, int>(node.Item1 + 1, node.Item2));
                visited[node.Item1 + 1, node.Item2] = true;
            }
            if (node.Item2 + 1 < col && !visited[node.Item1, node.Item2 + 1])
            {
                queue.Add(matrix[node.Item1, node.Item2 + 1], new Tuple<int, int>(node.Item1, node.Item2 + 1));
                visited[node.Item1, node.Item2 + 1] = true;
            }
        }
        return -1;
    }
}
/// <summary>
/// Comparer for comparing two keys, handling equality as beeing greater
/// Use this Comparer e.g. with SortedLists or SortedDictionaries, that don't allow duplicate keys
/// </summary>
/// <typeparam name="TKey"></typeparam>
public class DuplicateKeyComparer<TKey> : IComparer<TKey> where TKey : IComparable
{
    public int Compare(TKey x, TKey y)
    {
        int result = x.CompareTo(y);
        if (result == 0)
            return 1;   // Handle equality as beeing greater
        else
            return result;
    }
}
```

[Kth Smallest Element in a Sorted Matrix] - 20160930

## 436. Find Right Interval
>Use the list of anonymous types

```C#
public class Solution
{
    public int[] FindRightInterval(Interval[] intervals)
    {
        int[] ans = new int[intervals.Length];
        var tuples = new[] { new { start = intervals[0].start, end = intervals[0].end, position = 0 } }.ToList();
        for (int i = 1; i < intervals.Length; ++i)
            tuples.Add(new { start = intervals[i].start, end = intervals[i].end, position = i });
        tuples = tuples.OrderBy(o => o.start).ToList();
        foreach (var tuple in tuples)
        {
            int l = 0, r = tuples.Count - 1, mid = 0;
            while (l <= r)
            {
                mid = l + (r - l) / 2;
                if (tuples[mid].start == tuple.end) break;
                else if (tuples[mid].start > tuple.end) r = mid - 1;
                else l = mid + 1;
            }
            if (tuples[mid].start < tuple.end) ++mid;
            if (mid < tuples.Count && tuples[mid].start >= tuple.end)
                ans[tuple.position] = tuples[mid].position;
            else ans[tuple.position] = -1;
        }
        return ans;
    }
}
```
[Find Right Interval] - 20161101

## Basic operations on Binary Tree
### Traverse by level
```C#
IList<IList<int>> TraByLevelOrder = null;
public void Traverse(TreeNode node, int level)
{
    if (node == null)
        return;
    if (TraByLevelOrder.Count - 1 >= level)
    {
        if (node.left != null)
            TraByLevelOrder[level].Add(node.left.val);
        if (node.right != null)
            TraByLevelOrder[level].Add(node.right.val);
    }
    else
    {
        IList<int> list = new List<int>();
        if (node.left != null)
            list.Add(node.left.val);
        if (node.right != null)
            list.Add(node.right.val);
        if (list.Count > 0)
            TraByLevelOrder.Add(list);
    }
    Traverse(node.left, level + 1);
    Traverse(node.right, level + 1);
}
```
### Find Kth Smallest Element in a BST

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
[Eratosthenes-Sundaram-Atkins-Sieve-Implementation]:http://www.codeproject.com/Articles/490085/Eratosthenes-Sundaram-Atkins-Sieve-Implementation
[Counting Bits]:https://leetcode.com/problems/counting-bits/
[Kth Smallest Element in a Sorted Matrix]:https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
[House Robber III]:https://leetcode.com/problems/house-robber-iii/
[Combination Sum IV]:https://leetcode.com/problems/combination-sum-iv/
[Climbing Stairs]:https://leetcode.com/problems/climbing-stairs/
[Find Right Interval]:https://leetcode.com/problems/find-right-interval/
