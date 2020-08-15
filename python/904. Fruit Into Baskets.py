# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 16/8/2020 上午2:12
"""

from collections import defaultdict


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        left, right = 0, 0
        basket = defaultdict(int)
        ret, cur = 0, 0
        while right < len(tree):
            if len(basket) >= 2 and tree[right] not in basket:
                while True:
                    if len(basket) == 1:
                        break

                    basket[tree[left]] -= 1
                    cur -= 1
                    if basket[tree[left]] == 0:
                        del basket[tree[left]]
                    left += 1

            basket[tree[right]] += 1
            cur += 1
            right += 1
            ret = max(ret, cur)

        return ret