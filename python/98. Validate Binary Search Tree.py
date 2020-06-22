# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 22/6/2020 下午2:40
"""


class Solution:

    def valid(self, node):

        if not node:
            return True, 0, 0

        if node.left:
            flag, lmin, lmax = self.valid(node.left)
            if not flag or lmax >= node.val:
                return False, 0, 0
        else:
            lmin = node.val

        if node.right:
            flag, rmin, rmax = self.valid(node.right)
            if not flag or rmin <= node.val:
                return False, 0, 0
        else:
            rmax = node.val

        return True, lmin, rmax

    def isValidBST(self, root: TreeNode) -> bool:
        flag, _, __ = self.valid(root)
        return flag
