# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 8/8/2020 下午8:41
"""
from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        ng_L, ng_M = [], []
        cur_L, cur_M = sum(A[:L]), sum(A[:M])
        for i in range(L, len(A) + 1):
            ng_L.append({
                'pos': i - 1,
                'sum': cur_L
            })
            if i < len(A):
                cur_L = cur_L + A[i] - A[i - L]

        for i in range(M, len(A) + 1):
            ng_M.append({
                'pos': i - 1,
                'sum': cur_M
            })
            if i < len(A):
                cur_M = cur_M + A[i] - A[i - M]

        ng_L.sort(reverse=True, key=lambda x: x['sum'])
        ng_M.sort(reverse=True, key=lambda x: x['sum'])

        ret = 0
        for l in ng_L:
            for m in ng_M:
                if l['pos'] - L + 1 > m['pos'] or l['pos'] < m['pos'] - M + 1:
                    ret = max(ret, l['sum'] + m['sum'])
                    break

        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.maxSumTwoNoOverlap([8, 6, 7], 1, 1))
    print(s.maxSumTwoNoOverlap([2, 1, 5, 6, 0, 9, 5, 0, 3, 8], 4, 3))  # 31
    print(s.maxSumTwoNoOverlap([0, 6, 5, 2, 2, 5, 1, 9, 4], 1, 2))  # 20
    print(s.maxSumTwoNoOverlap([3, 8, 1, 3, 2, 1, 8, 9, 0], 3, 2))  # 29
