# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 12/8/2020 上午10:25
"""

from collections import defaultdict


class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        ret = 0
        n = minSize
        bucket = defaultdict(int)
        pi = 0
        for i in range(n, len(s) + 1):
            sub = s[pi:i]
            pi += 1
            if len(set(sub)) > maxLetters:
                continue
            bucket[sub] += 1

        # print(bucket)
        if len(bucket) > 0:
            ret = max(ret, max([v for k, v in bucket.items()]))

        return ret

    def maxFreq2(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        ret = 0
        for n in range(minSize, maxSize + 1):
            bucket = defaultdict(int)
            pi = 0
            for i in range(n, len(s) + 1):
                sub = s[pi:i]
                pi += 1
                if len(set(sub)) > maxLetters:
                    continue
                bucket[sub] += 1

            # print(bucket)
            if len(bucket) > 0:
                ret = max(ret, max([v for k, v in bucket.items()]))

        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.maxFreq("aababcaab", 2, 3, 4))
