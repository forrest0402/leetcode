# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 22/6/2020 上午11:15
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def divide_and_conquer(self, s, e):
        if s == e:
            return [TreeNode(s, None, None)]
        if s > e:
            return [None]

        ret = []
        for mid in range(s, e + 1):
            lefts = self.divide_and_conquer(s, mid - 1)
            rights = self.divide_and_conquer(mid + 1, e)
            for l in lefts:
                for r in rights:
                    root = TreeNode(mid, None, None)
                    root.left = l
                    root.right = r
                    ret.append(root)
        return ret

    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.divide_and_conquer(1, n)


if __name__ == "__main__":
    s = Solution()
    print(s.generateTrees(4))
