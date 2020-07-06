# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 7/7/2020 上午12:39
"""
import math
import random
from typing import List


class Solution:
    def valid(self, piles, k, H):
        s = 0
        for p in piles:
            s += math.ceil(p / k)
        return s <= H

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        start, end = 1, max(piles)

        while start <= end:
            k = (start + end) // 2
            if self.valid(piles, k, H):
                end = k - 1
            else:
                start = k + 1

        return start


if __name__ == "__main__":
    s = Solution()
    print(s.minEatingSpeed([9095], 2))
    print(s.minEatingSpeed(
        [9095, 7570, 5477, 1432, 927, 665, 8363, 8665, 5712, 2676, 2606, 9368, 5613, 7695, 7256, 8747, 7612, 3545, 5236,
         3762, 7760, 6337, 9251, 4257, 3575, 1601, 3282, 2191, 3866, 5026, 8964, 1385, 4617, 6057, 6367, 703, 1559,
         5098, 6461, 3770, 7141, 5709, 448, 1748, 5029, 3626, 33, 5274, 5865, 5837, 6680, 6794, 8387, 7936, 2382, 3931,
         7044, 3680, 7067, 1751, 2865, 8237, 3884, 5672, 5768, 511, 3806, 1938, 5631, 9305, 7620, 6543, 6712, 207, 3275,
         1696, 2600, 804, 6559, 5735, 7397, 7279, 8360, 6175, 3200, 7700, 726, 4239, 9155, 9108, 4683, 8687, 7032, 5827,
         5949, 357, 2415], 9482))

    n = random.randint(1000, 10000)
    piles = random.choices(list(range(n)), k=int(math.sqrt(n)))
    print(s.minEatingSpeed(piles, n * random.randint(1, 100)))
    print(s.minEatingSpeed([30, 11, 23, 4, 20], 5))
    assert s.minEatingSpeed([3, 6, 7, 11], 8) == 4
    assert s.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
    assert s.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23
