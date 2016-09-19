/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution
{
    public ListNode RemoveNthFromEnd(ListNode head, int n)
    {
        int count = 0;
        ListNode temp = head;
        while (temp != null)
        {
            temp = temp.next;
            ++count;
        }
        if (count == n)
            return head.next;
        temp = head;
        for (int i = 1; i < count - n; ++i)
            temp = temp.next;
        temp.next = temp.next.next;
        return head;
    }
}