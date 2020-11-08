# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 8/11/2020 下午8:13
"""

import heapq
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyHeap(object):
    def __init__(self, size, key=lambda x: x.val):
        self.key = key
        self.index = 0
        self._data = []

    def push(self, item):
        # print(self.key(item))
        heapq.heappush(self._data, (self.key(item), item))
        self.index += 1

    def pop(self):
        return heapq.heappop(self._data)[1]

    def empty(self):
        return len(self._data) <= 0


class Solution:
    def mergeKLists2(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None

        heap = MyHeap(len(lists))
        for item in lists:
            while item:
                heap.push(item.val)
                item = item.next

        head, tail = None, None
        while not heap.empty():
            ele = heap.pop()
            if tail:
                tail.next = ele
                tail = tail.next
            else:
                head = tail = ele

        tail.next = None
        return head

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None

        data = []
        for n in lists:
            while n:
                data.append(n.val)
                n = n.next
        heapq.heapify(data)

        if not data:
            return None

        head, tail = None, None
        while len(data) > 0:
            ele = ListNode(heapq.heappop(data))
            if tail:
                tail.next = ele
                tail = tail.next
            else:
                head = tail = ele

        tail.next = None
        return head


if __name__ == "__main__":
    s = Solution()
    inputs = [1, 8, 9, 10, 5, 4]
    inputs = [ListNode(x) for x in inputs]
    head = s.mergeKLists(inputs)
    while head:
        print(f'{head.val}\t')
        head = head.next
