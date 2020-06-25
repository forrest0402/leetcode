# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 26/6/2020 上午12:03
"""


class Solution:

    def dfs(self, x, y, z, cur_x, cur_y, visited):
        # print(cur_x, cur_y)
        key = "{}-{}".format(cur_x, cur_y)
        if key in visited:
            return False
        if cur_x < 0 or cur_x > x or cur_y < 0 or cur_y > y:
            return False

        if cur_x == z or cur_y == z or cur_x + cur_y == z or cur_x + y == z or cur_y + x == z:
            return True

        visited.add(key)

        # fill x
        if cur_x < x and cur_y < y:
            if self.dfs(x, y, z, x, cur_y, visited):
                return True

        # fill y
        if cur_y < y and cur_x < x:
            if self.dfs(x, y, z, cur_x, y, visited):
                return True

        # pour y into x
        if cur_y > 0 and cur_x < x:
            ncur_x, ncur_y = min(cur_x + cur_y, x), max(cur_x + cur_y - x, 0)
            if self.dfs(x, y, z, ncur_x, ncur_y, visited):
                return True

        # pour x into y
        if cur_x > 0 and cur_y < y:
            ncur_x, ncur_y = max(cur_x + cur_y - y, 0), min(cur_x + cur_y, y)
            if self.dfs(x, y, z, ncur_x, ncur_y, visited):
                return True

        # empty x
        if cur_x > 0:
            if self.dfs(x, y, z, 0, cur_y, visited):
                return True

        # empty y
        if cur_y > 0:
            if self.dfs(x, y, z, cur_x, 0, visited):
                return True

        return False

    def canMeasureWater2(self, x: int, y: int, z: int) -> bool:
        return self.dfs(x, y, z, 0, 0, set())

    def gcd(self, a, b):
        while b != 0:
            temp = b
            b = a % b
            a = temp

        return a

    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False
        if x == z or y == z or x + y == z:
            return True

        print(self.gcd(x, y))
        return z % self.gcd(x, y) == 0
