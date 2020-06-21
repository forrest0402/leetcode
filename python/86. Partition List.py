# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 21/6/2020 下午8:53
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def partition(self, head: ListNode, x: int) -> ListNode:
        start, cur = None, None
        tail, ctail = None, None

        while head:
            if head.val < x:
                if cur is None:
                    start = cur = head
                else:
                    cur.next = head
                    cur = cur.next
            else:
                if ctail is None:
                    tail = ctail = head
                else:
                    ctail.next = head
                    ctail = ctail.next

            head = head.next

        if ctail:
            ctail.next = None

        if not cur:
            return tail

        cur.next = tail

        return start


if __name__ == "__main__":
    s = Solution()

