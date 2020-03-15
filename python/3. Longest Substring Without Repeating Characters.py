# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 15/3/2020 下午11:32
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0
        max_len = 1
        res = s[0]
        visit = dict()
        pre = 0
        for i, v in enumerate(s):
            if v not in visit or visit[v] < pre:
                if i + 1 - pre >= max_len:
                    max_len = i + 1 - pre
                    res = s[pre:i + 1]
            else:
                pre = visit[v] + 1
            visit[v] = i

        return len(res)


if __name__ == "__main__":
    s = Solution()
    # print(s.lengthOfLongestSubstring("pwwkewp"))
    assert s.lengthOfLongestSubstring("fkkasfkwerzvnxcvkjsdflkjqwerkljzslkfjasfdhzxvnzxcjvklsjdfkjlasfdj") == 12
