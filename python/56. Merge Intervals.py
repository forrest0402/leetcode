# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 17/6/2020 上午1:01
"""
from typing import List


class Node(object):

    def __init__(self, minv, maxv):
        self.left = None
        self.right = None
        self.minv = minv
        self.maxv = maxv
        self.check = False


class Solution:

    def interact(self, interval: List[int], node: Node) -> int:
        if interval[0] >= node.minv and interval[1] <= node.maxv:
            return 0

        if interval[0] <= node.minv and interval[1] >= node.maxv:
            node.check = True
            node.minv, node.maxv = interval

        if (node.minv <= interval[0] <= node.maxv) or (node.minv <= interval[1] <= node.maxv):
            node.check = True
            node.minv = min(node.minv, interval[0])
            node.maxv = max(node.maxv, interval[1])
            return 0

        if node.minv > interval[1]:
            return -1
        return 1

    def traverse(self, node: Node) -> List[List[int]]:
        if node is None:
            return []

        if node.left is None and node.right is None:
            return [[node.minv, node.maxv]]

        lr = self.traverse(node.left)
        rr = self.traverse(node.right)
        if not node.check:
            return [[node.minv, node.maxv]] + lr + rr

        result = []
        for i, l in enumerate(lr):
            if node.minv <= l[0] <= node.maxv or node.minv <= l[1] <= node.maxv:
                node.minv = min(node.minv, l[0])
            else:
                result.append(l)

        for i, r in enumerate(rr[::-1]):
            if node.minv <= r[0] <= node.maxv or node.minv <= r[1] <= node.maxv:
                node.maxv = max(node.maxv, r[1])
            else:
                result.append(r)
        result.append([node.minv, node.maxv])
        return result

    def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return intervals
        idx = len(intervals) // 2
        root = Node(*intervals[idx])
        for i, interval in enumerate(intervals):
            if i == idx:
                continue

            node = root
            while True:
                ret = self.interact(interval, node)
                if ret == 0:
                    break
                if ret == -1:
                    if node.left is None:
                        node.left = Node(*interval)
                        break
                    node = node.left
                else:
                    if node.right is None:
                        node.right = Node(*interval)
                        break
                    node = node.right

        result = self.traverse(root)
        return result

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals = sorted(intervals, key=lambda i: i[0])
        for i in intervals:
            if not result:
                result.append(i)
            else:
                if i[0] <= result[-1][1]:
                    result[-1][1] = max(result[-1][1], i[1])
                else:
                    result.append(i)

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.merge([[3, 3], [3, 5], [1, 3], [2, 4], [0, 0], [4, 6], [2, 2], [1, 2], [3, 3], [4, 4]]))
    print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(s.merge([[1, 4], [4, 5]]))
    print(s.merge([[2, 3], [4, 6], [5, 7], [3, 4]]))
