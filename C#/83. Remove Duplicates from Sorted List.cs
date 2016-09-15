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
    public ListNode DeleteDuplicates(ListNode head)
    {
        ListNode t1 = head;
        while (t1 != null)
        {
            ListNode t2 = t1;
            while (t2.next != null)
            {
                if (t2.next.val == t1.val)
                    t2.next = t2.next.next;
                else t2 = t2.next;
            }
            t1 = t1.next;
        }
        return head;
    }
}