# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 24/3/2020 下午11:32
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first, second = head, head
        while n > 0 and second is not None:
            second = second.next
            n -= 1
        if second is None:
            return head.next

        while second.next is not None:
            second = second.next
            first = first.next

        first.next = first.next.next
        return head
