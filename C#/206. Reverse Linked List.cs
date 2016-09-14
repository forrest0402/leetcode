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
    public ListNode ReverseList(ListNode head)
    {
        if (head == null)
            return null;
        bool first = true;
        int lPos = 0, rPos = 0;
        ListNode ans = head;
        while (lPos < rPos || first)
        {
            if (first)
            {
                ListNode temp = head;
                while (temp.next != null)
                {
                    temp = temp.next;
                    ++rPos;
                }
                int swapInt = head.val;
                head.val = temp.val;
                temp.val = swapInt;
                first = false;
                ++lPos;
                --rPos;
                head = head.next;
            }
            else
            {
                ListNode temp = head;
                for (int i = 0; i < rPos - lPos; ++i)
                    temp = temp.next;
                int swapInt = head.val;
                head.val = temp.val;
                temp.val = swapInt;
                ++lPos;
                --rPos;
                head = head.next;
            }
        }
        return ans;
    }
}