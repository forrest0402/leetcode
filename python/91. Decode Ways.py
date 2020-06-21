# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 22/6/2020 上午12:15
"""


class Solution:

    def dfs(self, s, idx, cur, ret):
        if idx == len(s):
            ret.append(cur)
            return

        if s[idx] != '0':
            self.dfs(s, idx + 1, cur + [s[idx]], ret)
        if len(cur) > 0 and 1 <= int(cur[-1] + s[idx]) <= 26:
            cur[-1] += s[idx]
            self.dfs(s, idx + 1, cur, ret)

    def numDecodings2(self, s: str) -> int:
        if len(s) == 0:
            return 0

        for i, ss in enumerate(s):
            if ss == '0':
                if i <= 0:
                    return 0
                if s[i - 1] != '1' and s[i - 1] != '2':
                    return 0

        ret = []
        self.dfs(s, 0, [], ret)
        print(ret)
        return len(ret)

    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0

        for i, ss in enumerate(s):
            if ss == '0':
                if i <= 0:
                    return 0
                if s[i - 1] != '1' and s[i - 1] != '2':
                    return 0

        dp1 = [1 for _ in range(len(s))]
        dp2 = [0 for _ in range(len(s))]
        for i in range(1, len(s)):
            dp1[i] = dp1[i - 1] + dp2[i - 1] if s[i] != '0' else 0
            dp2[i] = dp1[i - 1] if 1 <= int(s[i - 1] + s[i]) <= 26 else 0

        return dp1[-1] + dp2[-1]


if __name__ == "__main__":
    s = Solution()
    arg = "10"
    print(s.numDecodings(arg))
    print(s.numDecodings2(arg))
