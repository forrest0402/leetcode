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
    public ListNode SwapPairs(ListNode head)
    {
        int count = 0;
        ListNode ans = head;
        ListNode pre = null;
        while (head != null && head.next != null)
        {
            if (count % 3 != 0)
            {
                head = head.next;
                ++count;
                continue;
            }
            ListNode temp = head;
            head = head.next;
            temp.next = head.next;
            head.next = temp;
            if (pre != null)
                pre.next = head;
            pre = temp;
            if (count == 0)
                ans = head;
            ++count;
        }
        return ans;
    }
}