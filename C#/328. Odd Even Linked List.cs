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
    public ListNode OddEvenList(ListNode head)
    {
        if (head == null || head.next == null)
            return head;
        ListNode odd = head, even = head.next, oTail = null, eHead = head.next;
        while (odd != null && even != null)
        {
            odd.next = even.next;
            even.next = odd.next == null ? null : odd.next.next;
            if (odd.next == null)
                oTail = odd;
            odd = odd.next;
            even = even.next;
        }
        if (oTail == null)
            odd.next = eHead;
        else oTail.next = eHead;
        return head;
    }
}