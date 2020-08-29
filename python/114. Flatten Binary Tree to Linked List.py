# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 30/8/2020 上午12:37
"""


class Solution:

    def preorder(self, node):

        if not node:
            return None, None

        right = node.right

        left_root, left_rightmost = self.preorder(node.left)
        if left_root:
            node.right = left_root
            left_rightmost.right, right_rightmost = self.preorder(right)

        else:
            node.right, right_rightmost = self.preorder(right)

        if not right_rightmost:
            right_rightmost = left_rightmost

        node.left = None

        # print(node, right_rightmost)
        return node, right_rightmost if right_rightmost else node

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.preorder(root)

