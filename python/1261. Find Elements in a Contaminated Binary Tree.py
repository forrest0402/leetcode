# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 10/8/2020 上午8:43
"""


class FindElements:

    def __traverse(self, node, nodes):
        if not node:
            return

        nodes.add(node.val)
        if node.left:
            node.left.val = node.val * 2 + 1
            self.__traverse(node.left, nodes)

        if node.right:
            node.right.val = node.val * 2 + 2
            self.__traverse(node.right, nodes)

    def __init__(self, root: TreeNode):
        self.nodes = set()
        root.val = 0
        self.__traverse(root, self.nodes)

    def find(self, target: int) -> bool:
        # level = math.floor(math.log2(target+1))
        return target in self.nodes
