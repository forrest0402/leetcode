# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 25/7/2020 下午5:11
"""

from typing import List


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
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
    s = Solution()
    # [true,false,true,true,false]
    print(s.camelMatch(["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], "FB"))
    #  [true,false,true,false,false]
    print(s.camelMatch(["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], "FoBa"))
    # [false,true,false,false,false]
    print(s.camelMatch(["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], "FoBaT"))
