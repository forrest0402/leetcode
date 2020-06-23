# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 24/6/2020 上午2:11
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def dfs(self, node, k) -> (TreeNode, int):
        if not node:
            return None, 0

        if not node.left and not node.right:
            if k <= 1:
                return node, 1
            else:
                return None, 1

        lnode, lsize = self.dfs(node.left, k)
        if lnode:
            return lnode, -1

        if lsize + 1 == k:
            return node, -1

        rnode, rsize = self.dfs(node.right, k - lsize - 1)
        if rnode:
            return rnode, -1

        return None, lsize + rsize + 1

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        node, _ = self.dfs(root, k)
        return node.val
