# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 28/8/2020 上午9:34
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def distributeCoins(self, root: TreeNode) -> int:
        ans = 0

        def dfs(node):
            global ans
            if not node:
                return 0

            left, right = dfs(node.left), dfs(node.right)

            ans = ans + abs(left) + abs(right)

            return node.val + left + right - 1

        dfs(root)
        return ans


if __name__ == "__main__":
    root = TreeNode()
    s = Solution()
    print(s.distributeCoins(root))
