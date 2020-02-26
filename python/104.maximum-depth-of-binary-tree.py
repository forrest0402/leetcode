# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 26/2/2020 下午11:53
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, node):
        if node is None:
            return 0;
        return max(self.dfs(node.left), self.dfs(node.right)) + 1

    def maxDepth(self, root: TreeNode) -> int:
        return self.dfs(root)
