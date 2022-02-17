# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project__ =  'leetcode'
__file__    =  '__init__.py.py'
__author__  =  'king'
__time__    =  '2022/2/14 19:15'


                              _ooOoo_
                             o8888888o
                             88" . "88
                             (| -_- |)
                             O\  =  /O
                          ____/`---'\____
                        .'  \\|     |//  `.
                       /  \\|||  :  |||//  \
                      /  _||||| -:- |||||-  \
                      |   | \\\  -  /// |   |
                      | \_|  ''\---/''  |   |
                      \  .-\__  `-`  ___/-. /
                    ___`. .'  /--.--\  `. . __
                 ."" '<  `.___\_<|>_/___.'  >'"".
                | | :  `- \`.;`\ _ /`;.`/ - ` : | |
                \  \ `-.   \_ __\ /__ _/   .-` /  /
           ======`-.____`-.___\_____/___.-`____.-'======
                              `=---='
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                       佛祖保佑        永无BUG
"""
from typing import List

from leetcode.utils.timeutils import time_interval

"""
难度：中等

假设你有一个长度为n的数组，初始情况下所有的数字均为0，你将会被给出k个更新的操作。

其中，每个操作会被表示为一个三元组：[startIndex, endIndex, inc]，
你需要将子数组 A[startIndex ... endIndex]（包括 startIndex 和 endIndex）增加 inc。

请你返回k次操作后的数组。

示例:
    输入: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
    输出: [-2,0,3,5,3]
解释:
    初始状态:
    [0,0,0,0,0]

    进行了操作 [1,3,2] 后的状态:
    [0,2,2,2,0]

    进行了操作 [2,4,3] 后的状态:
    [0,2,5,5,3]

    进行了操作 [0,2,-2] 后的状态:
    [-2,0,3,5,3]

Related Topics 数组 差分数组
"""


class Difference:
    def __init__(self, nums):
        self.diff = [0] * len(nums)
        self.diff[0] = nums[0]
        for i in range(1, len(nums)):
            self.diff[i] = nums[i] - nums[i - 1]

    def increment(self, i, j, val):
        self.diff[i] += val
        if j + 1 < len(self.diff):
            self.diff[j + 1] -= val

    def result(self):
        r = [0] * len(self.diff)
        r[0] = self.diff[0]
        for i in range(1, len(self.diff)):
            r[i] = r[i - 1] + self.diff[i]
        return r


class Solution:

    @staticmethod
    @time_interval
    def getModifiedArray(length: int, updates: List[List[int]]) -> List[int]:
        if length <= 0:
            return []
        result = [0] * (length + 1)
        for start, end, inc in updates:
            result[start] += inc
            result[end + 1] -= inc
        for i in range(1, length):
            result[i] += result[i - 1]
        return result[:-1]

    @staticmethod
    @time_interval
    def getModifiedArray2(length: int, updates: List[List[int]]) -> List[int]:
        nums = [0] * length
        d = Difference(nums)
        for start, end, inc in updates:
            d.increment(start, end, inc)
        return d.result()


updates = [[1, 3, 2], [2, 4, 3], [0, 2, -2]]
s = Solution()

print(s.getModifiedArray(5, updates))
print(s.getModifiedArray2(5, updates))
