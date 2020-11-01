# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 29/9/2020 上午1:36
"""
from collections import defaultdict
from typing import List


class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        task_map = defaultdict(int)
        for task in tasks:
            task_map[task] += 1

        keys = list(task_map.keys())
        keys.sort(key=lambda x: task_map[x], reverse=True)

        ret = 0
        while keys:
            i, idx = -1, -1
            finished_tasks = set()
            while i < n and len(keys) > 0:
                i += 1
                idx += 1
                ret += 1

                key_idx = idx % len(keys)
                key = keys[key_idx]

                if key in finished_tasks:
                    continue
                task_map[key] -= 1
                if task_map[key] == 0:
                    del task_map[key]
                    del keys[key_idx]
                    idx -= 1

                finished_tasks.add(key)

            keys.sort(key=lambda x: task_map[x], reverse=True)
            # print("********************")
            # print('keys', keys)
            # print(task_map)
            # print(ret)
            # print('exec: ', finished_tasks)

        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2))  # 16
    print(s.leastInterval(["A", "A", "A", "B", "B", "B"], 2))  # 8
    print(s.leastInterval(["A", "A", "A", "B", "B", "B"], 0))  # 6
    print(s.leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 4))  # 26
