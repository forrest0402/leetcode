# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 15/8/2020 下午3:27
"""

from collections import defaultdict
from typing import List


class Solution:
    def trap2(self, height: List[int]) -> int:
        dicts = defaultdict(list)
        for i, h in enumerate(height):
            for l in range(1, h + 1):
                dicts[l].append(i)

        ret = 0
        for k, v in dicts.items():
            if len(v) > 0:
                print("{}/{}".format(k, v[-1] - v[0] + 1 - len(v)))
                ret += v[-1] - v[0] + 1 - len(v)

        return ret

    def find(self, nums, target, arr):
        left, right = 0, len(arr) - 1
        if target < arr[left]:
            return nums[arr[left]]
        if target > arr[right]:
            return nums[arr[right]]
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return nums[target]

            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        if arr[mid] < target:
            return nums[max(arr[mid], arr[mid + 1])]
        else:
            return nums[max(arr[mid], arr[mid - 1])]

    def trap(self, height: List[int]) -> int:
        if not height or len(height) == 1:
            return 0

        cd = defaultdict(int)
        min_i = dict()
        max_i = dict()
        max_h = 0
        inc_pre = height[0] - 1
        for i, h in enumerate(height):
            if h == 0:
                continue
            cd[h] += 1
            max_h = max(max_h, h)
            if h > inc_pre:
                min_i[h] = i
                inc_pre = h

        for i, h in enumerate(height):
            if i < min_i[max_h]:
                continue

            for key in list(max_i.keys()):
                if key < h:
                    del max_i[key]

            max_i[h] = i

        csum = [-1 for _ in range(max_h + 1)]
        hy = sorted(cd.keys(), reverse=True)
        cur_sum = 0
        for h in hy:
            cur_sum += cd[h]
            csum[h] = cur_sum

        pre = 0
        for i in range(max_h, 0, -1):
            if csum[i] == -1:
                csum[i] = pre
            pre = csum[i]

        ret = 0
        arr_de = list(max_i.keys())
        arr_de.sort()
        arr_in = list(min_i.keys())
        arr_in.sort()
        for i in range(1, max_h + 1):
            print(1 - csum[i] + self.find(max_i, i, arr_de) - self.find(min_i, i, arr_in))
            ret += 1 - csum[i] + self.find(max_i, i, arr_de) - self.find(min_i, i, arr_in)

        return ret


if __name__ == "__main__":
    s = Solution()
    # print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    # 322
    print(s.trap([105, 7, 90, 13, 296, 48, 139, 152]))
    # 174801674
    print(s.trap([0]))
