# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 25/7/2020 下午5:11
"""

from typing import List

import numpy as np
import tensorflow as tf


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        ret = []
        for query in queries:
            idx = 0
            for q in query:
                if 'A' <= q <= 'Z':
                    if idx >= len(pattern) or q != pattern[idx]:
                        idx = -1
                        break
                    idx += 1
                else:
                    if idx >= len(pattern):
                        continue
                    if q == pattern[idx]:
                        idx += 1

            ret.append(idx == len(pattern))

        return ret

    def camelMatch2(self, queries: List[str], pattern: str) -> List[bool]:
        ret = []
        trim_p = [p for p in pattern if 'A' <= p <= 'Z']
        for query in queries:
            trim_q = [q for q in query if 'A' <= q <= 'Z']
            if trim_p != trim_q:
                ret.append(False)
            else:
                idx = 0
                for q in query:
                    if idx < len(pattern) and q == pattern[idx]:
                        idx += 1

                ret.append(idx == len(pattern))

        return ret


if __name__ == "__main__":
    a = np.array([0.6**5*0.4**5, (0.5**5)**2])
    print(a)
    print(a/np.sum(a))
    print(tf.nn.softmax(a))

    s = Solution()
    # [true,false,true,true,false]
    print(s.camelMatch(["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], "FB"))
    #  [true,false,true,false,false]
    print(s.camelMatch(["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], "FoBa"))
    # [false,true,false,false,false]
    print(s.camelMatch(["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], "FoBaT"))
