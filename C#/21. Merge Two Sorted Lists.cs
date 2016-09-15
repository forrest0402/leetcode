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
    public ListNode MergeTwoLists(ListNode l1, ListNode l2)
    {
        ListNode head = null, last = null;
        while (l1 != null || l2 != null)
        {
            if (l1 == null || (l2 != null && l1.val > l2.val))
            {
                if (head == null)
                {
                    head = new ListNode(l2.val);
                    last = head;
                }
                else
                {
                    last.next = new ListNode(l2.val);
                    last = last.next;
                }
                l2 = l2.next;
            }
            else if (l2 == null || l1.val <= l2.val)
            {
                if (head == null)
                {
                    head = new ListNode(l1.val);
                    last = head;
                }
                else
                {
                    last.next = new ListNode(l1.val);
                    last = last.next;
                }
                l1 = l1.next;
            }
        }
        return head;
    }
}