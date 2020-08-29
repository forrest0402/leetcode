# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 29/8/2020 下午4:43
"""

from collections import defaultdict


class Solution:

    def widthOfBinaryTree(self, root: TreeNode) -> int:
        ret = 0
        levels = []

        def dfs(node, val, level, levels):
            if not node:
                return

            if len(levels) <= level:
                levels.append([])

            levels[level].append(val)

            dfs(node.left, val * 2, level + 1, levels)
            dfs(node.right, val * 2 + 1, level + 1, levels)

        dfs(root, 1, 0, levels)
        # print(levels)
        for l in levels:
            if len(l) == 1:
                ret = max(ret, 1)
            else:
                ret = max(ret, l[-1] - l[0] + 1)

        return ret
