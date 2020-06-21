# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 22/6/2020 上午1:50
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        nhead, ntail = None, None
        next = head
        idx = 1
        rhead, rtail = None, None
        while next:
            next = head.next
            if m == idx:
                rhead = rtail = head
            elif m < idx <= n:
                head.next = rhead
                rhead = head
            else:
                if not nhead:
                    nhead = ntail = head
                    if rhead:
                        nhead = rhead
                        ntail = rtail.next = head
                        rhead = None
                        rtail = None
                else:
                    if rhead:
                        ntail.next = rhead
                        rtail.next = head
                        ntail = head
                        rhead = None
                        rtail = None
                    else:
                        ntail.next = head
                        ntail = head

            idx += 1
            head = next

        if rtail:
            rtail.next = None

        if rhead:
            if nhead:
                ntail.next = rhead
            else:
                return rhead

        return nhead if nhead else rhead
