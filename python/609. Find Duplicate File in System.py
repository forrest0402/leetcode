# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 4/7/2020 下午6:17
"""


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        ret = dict()
        for path in paths:
            array = path.split(' ')
            for i in range(1, len(array)):
                idx = array[i].index('(')
                fpath = "{}/{}".format(array[0], array[i][0:idx])
                key = array[i][idx + 1:-1]

                if key not in ret:
                    ret[key] = [fpath]
                else:
                    ret[key].append(fpath)

        return [v for k, v in ret.items() if len(v) >= 2]
