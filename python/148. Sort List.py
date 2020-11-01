# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 2/11/2020 上午1:26
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


import random


class Solution:
    MIN_INT = -2 ** 31
    MAX_INT = 2 ** 31

    def quick_sort(self, node, length):
        if not node:
            return None, None

        if not node.next:
            return node, node

        rand_length = random.randint(0, length - 1)
        pivot = node
        while rand_length > 0:
            pivot = pivot.next
            rand_length -= 1

        hl, hr, tl, tr = None, None, None, None
        max_l, max_r, min_l, min_r = self.MIN_INT, self.MIN_INT, self.MAX_INT, self.MAX_INT

        n = node
        num_l, num_r = 0, 0

        while n:
            if n == pivot:
                n = n.next
                continue
            if n.val < pivot.val:
                if tl:
                    tl.next = n
                    tl = tl.next
                else:
                    hl = tl = n
                num_l += 1
                if n.val < min_l:
                    min_l = n.val
                if n.val > max_l:
                    max_l = n.val
            else:
                if tr:
                    tr.next = n
                    tr = tr.next
                else:
                    hr = tr = n
                num_r += 1
                if n.val < min_r:
                    min_r = n.val
                if n.val > max_r:
                    max_r = n.val
            n = n.next

        if tl:
            tl.next = None
        if tr:
            tr.next = None

        if min_l == max_l:
            sorted_lhead, sorted_ltail = hl, tl
        else:
            sorted_lhead, sorted_ltail = self.quick_sort(hl, num_l)

        if min_r == max_r:
            sorted_rhead, sorted_rtail = hr, tr
        else:
            sorted_rhead, sorted_rtail = self.quick_sort(hr, num_r)

        pivot.next = sorted_rhead
        if sorted_ltail:
            sorted_ltail.next = pivot
            return sorted_lhead, sorted_rtail if sorted_rtail else pivot

        return pivot, sorted_rtail if sorted_rtail else pivot

    def sortList(self, head: ListNode) -> ListNode:
        length = 0
        n = head
        while n:
            n = n.next
            length += 1
        head, tail = self.quick_sort(head, length)
        return head
