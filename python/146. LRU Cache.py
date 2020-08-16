# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 16/8/2020 下午5:29
"""


class LRUCache:

    def __init__(self, capacity: int):
        self.data = dict()
        self.freq = dict()
        self.cap = capacity
        self.inc = 0

    def _inc(self):
        self.inc += 1
        return self.inc

    def get(self, key: int) -> int:
        if key in self.data:
            self.freq[key] = self._inc()
            return self.data[key]

        return -1

    def put(self, key: int, value: int) -> None:
        self.data[key] = value
        self.freq[key] = self._inc()

        if len(self.freq) > self.cap:
            dk, _ = min(self.freq.items(), key=lambda x: x[1])
            del self.data[dk]
            del self.freq[dk]
            # print(dk)


if __name__ == "__main__":
    obj = LRUCache(2)
    obj.put(1, 1)
    obj.put(2, 2)
    obj.get(1)
    obj.put(3, 3)

    print(obj.get(2))
    obj.put(4, 4)
    print(obj.get(3))
