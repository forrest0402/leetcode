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
    public ListNode RemoveElements(ListNode head, int val)
    {
        if (head == null)
            return null;
        ListNode ans = head;
        while (ans.next != null)
        {
            if (ans.next.val == val)
                ans.next = ans.next.next;
            else ans = ans.next;
        }
        if (head.val == val)
            head = head.next;
        return head;
    }
}