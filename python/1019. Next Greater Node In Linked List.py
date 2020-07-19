# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 20/7/2020 上午12:54
"""
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def nextLargerNodes(self, head: ListNode) -> List[int]:
        ret = []
        un_match = []
        found = False
        last_n = 10 ** 9
        while head:
            idx = len(ret)
            ret.append(0)
            if not (head.val <= last_n and not found):
                found = False
                while len(un_match) > 0:
                    (v, i) = un_match[-1]
                    if head.val > v:
                        ret[i] = head.val
                        found = True
                        un_match.pop()
                    else:
                        break

            un_match.append((head.val, idx))
            last_n = head.val
            head = head.next

        return ret

    def nextLargerNodes2(self, head: ListNode) -> List[int]:
        ret = []
        un_match = dict()
        found = False
        last_n = 10 ** 9
        while head:
            idx = len(ret)
            ret.append(0)
            if not (head.val <= last_n and not found):
                found = False
                for k, v in list(un_match.items()):
                    if head.val > v:
                        ret[k] = head.val
                        un_match.pop(k, None)
                        found = True

            un_match[idx] = head.val
            last_n = head.val
            head = head.next

        return ret
