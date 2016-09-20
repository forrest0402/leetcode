/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
 //not a proper solution
public class Solution
{
    public bool IsPalindrome(ListNode head)
    {
        if (head == null)
            return true;
        Stack<int> stack = new Stack<int>();
        ListNode t = head;
        while (t != null)
        {
            stack.Push(t.val);
            t = t.next;
        }
        t = head;
        while (t != null)
        {
            if (t.val != stack.Peek())
                return false;
            stack.Pop();
            t = t.next;
        }
        return true;
    }
}