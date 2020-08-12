# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 13/8/2020 上午12:18
"""


class Solution:

    def findTheLongestSubstring(self, s: str) -> int:
        vowl_to_bit_index = {
            'a': 1,
            'e': 2,
            'i': 4,
            'o': 8,
            'u': 16
        }
        state_to_index = {
            0: -1
        }

        state, max_len = 0, 0
        for i, cur in enumerate(s):
            if cur in vowl_to_bit_index:
                bit_to_flip = vowl_to_bit_index[cur]
                state ^= bit_to_flip

            if state not in state_to_index:
                state_to_index[state] = i

            max_len = max(max_len, i - state_to_index[state])

        return max_len


if __name__ == "__main__":
    s = Solution()
    print(s.findTheLongestSubstring("eleetminicoworoep"))  # 13
