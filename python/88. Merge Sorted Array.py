# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 26/2/2020 下午2:54
"""
from typing import List
import numpy as np


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:] = nums2[:]
        else:
            idx1, idx2, idx3 = m - 1, n - 1, m + n - 1
            while idx1 >= 0 and idx2 >= 0:
                if nums1[idx1] > nums2[idx2]:
                    nums1[idx3] = nums1[idx1]
                    idx1 -= 1
                else:
                    nums1[idx3] = nums2[idx2]
                    idx2 -= 1
                idx3 -= 1

            if idx2 >= 0:
                nums1[:idx2 + 1] = nums2[:idx2 + 1]


if __name__ == "__main__":
    s = Solution()
    nums1 = [2, 0]
    m = 1
    nums2 = [1]
    n = 1
    s.merge(nums1, m, nums2, n)
    print(nums1)

    nums1 = [4, 5, 6, 0, 0, 0]
    m = 3
    nums2 = [1, 2, 3]
    n = 3
    s.merge(nums1, m, nums2, n)
    print(nums1)

    nums1 = [4, 0, 0, 0, 0, 0]
    m = 1
    nums2 = [1, 2, 3, 5, 6]
    n = 5
    s.merge(nums1, m, nums2, n)
    print(nums1)

    nums1 = [6, 0, 0, 0, 0, 0]
    m = 1
    nums2 = [1, 2, 3, 4, 5]
    n = 5
    s.merge(nums1, m, nums2, n)
    print(nums1)

    nums1 = [1, 0, 0, 0, 0, 0]
    m = 1
    nums2 = [2, 3, 4, 5, 6]
    n = 5
    s.merge(nums1, m, nums2, n)
    print(nums1)

    nums1 = [1, 2, 6, 0, 0, 0]
    m = 3
    nums2 = [3, 4, 5]
    n = 3
    s.merge(nums1, m, nums2, n)
    print(nums1)

    nums1 = [1, 2, 3, 4, 5, 6]
    m = 4
    nums2 = []
    n = 0
    s.merge(nums1, m, nums2, n)
    print(nums1)

    nums1 = [2, 3, 4, 5, 6, 0]
    m = 5
    nums2 = [1]
    n = 1
    s.merge(nums1, m, nums2, n)
    print(nums1)

    nums1 = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
    m = 6
    nums2 = [1, 2, 2]
    n = 3
    s.merge(nums1, m, nums2, n)
    print(nums1)

    nums1 = [-1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0]
    m = 5
    nums2 = [-1, -1, 0, 0, 1, 2]
    n = 6
    s.merge(nums1, m, nums2, n)
    print(nums1)

    nums1 = [-10, -10, -9, -9, -9, -8, -8, -7, -7, -7, -6, -6, -6, -6, -6, -6, -6, -5, -5, -5, -4, -4, -4, -3, -3, -2,
             -2, -1, -1, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 9, 9, 9, 9, 0, 0, 0, 0, 0, 0,
             0, 0,
             0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    m = 55
    nums2 = [-10, -10, -9, -9, -9, -9, -8, -8, -8, -8, -8, -7, -7, -7, -7, -7, -7, -7, -7, -6, -6, -6, -6, -5, -5, -5,
             -5, -5,
             -4, -4, -4, -4, -4, -3, -3, -3, -2, -2, -2, -2, -2, -2, -2, -1, -1, -1, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2,
             2, 2,
             2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 9,
             9, 9,
             9]
    n = 99
    s.merge(nums1, m, nums2, n)
    print(nums1)
    a = [-10, -10, -10, -10, -9, -9, -9, -9, -9, -9, -9, -8, -8, -8, -8, -8, -8, -8, -7, -7, -7, -7, -7, -7, -7, -7, -7,
         -7, -7, -6, -6, -6, -6, -6, -6, -6, -6, -6, -6, -6, -5, -5, -5, -5, -5, -5, -5, -5, -4, -4, -4, -4, -4, -4, -4,
         -4, -3, -3, -3, -3, -3, -2, -2, -2, -2, -2, -2, -2, -2, -2, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1,
         1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 6,
         6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9]
    print(a)
    print(np.equal(a, nums1))
