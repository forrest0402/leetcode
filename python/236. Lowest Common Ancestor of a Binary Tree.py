# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 24/6/2020 上午11:44
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def contains(self, cur, target):

        if not cur:
            return False

        if cur.val == target.val:
            return True

        return self.contains(cur.left, target) or self.contains(cur.right, target)

    def dfs(self, cur, p, q):

        if not cur:
            return False, False, None

        if cur.val == p.val:
            if self.contains(cur, q):
                return True, True, cur
            return True, False, None

        if cur.val == q.val:
            if self.contains(cur, p):
                return True, True, cur
            return False, True, None

        lp, lq, ret = self.dfs(cur.left, p, q)
        if lp and lq:
            return True, True, ret

        rp, rq, ret = self.dfs(cur.right, p, q)
        if rp and rq:
            return True, True, ret

        # print(lp, lq, rp, rq)
        if (lp and rq) or (lq and rp):
            return True, True, cur

        if lp or rp:
            return True, False, None

        if lq or rq:
            return False, True, None

        return False, False, None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        _, __, ret = self.dfs(root, p, q)
        return ret
