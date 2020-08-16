# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 16/8/2020 下午6:25
"""


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        first = head
        while fast:

            fast = fast.next
            if not fast:
                return None

            fast = fast.next

            slow = slow.next

            if fast == slow:
                while first != slow:
                    first = first.next
                    slow = slow.next

                return first

        return None
