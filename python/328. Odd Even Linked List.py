# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 25/6/2020 下午3:14
"""


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        node, flag, even_head, even_tail = head.next, True, None, None
        odd_head = odd_tail = head
        while node:

            if flag:
                if not even_tail:
                    even_head = even_tail = node
                else:
                    even_tail.next = node
                    even_tail = node
            else:
                odd_tail.next = node
                odd_tail = node

            flag = not flag
            node = node.next

        if even_tail:
            even_tail.next = None
        odd_tail.next = even_head
        return head
