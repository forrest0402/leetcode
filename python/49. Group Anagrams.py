# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 15/6/2020 上午12:14
"""

from typing import List


class Solution:
    prime_number = {
        0: 2,
        1: 3,
        2: 5,
        3: 7,
        4: 11,
        5: 13,
        6: 17,
        7: 19,
        8: 23,
        9: 29,
        10: 31,
        11: 37,
        12: 41,
        13: 43,
        14: 47,
        15: 53,
        16: 59,
        17: 61,
        18: 67,
        19: 71,
        20: 73,
        21: 79,
        22: 83,
        23: 89,
        24: 97,
        25: 101,
        26: 113
    }

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def prime(c: str):
            i = ord(c) - ord('a')
            return self.prime_number[i]

        def hash(text):
            sum = 1
            for t in text:
                sum *= prime(t)
            return sum

        bucket = dict()
        for text in strs:
            key = hash(text)
            if key in bucket:
                bucket[key].append(text)
            else:
                bucket[key] = [text]

        return [v for k, v in bucket.items()]


if __name__ == "__main__":
    s = Solution()
    res = s.groupAnagrams(['ago', 'dem', 'ago'])
    res.sort()
    print(res)
