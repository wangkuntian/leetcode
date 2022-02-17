# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project__ =  'leetcode'
__file__    =  '__init__.py.py'
__author__  =  'king'
__time__    =  '2022/2/16 14:17'


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

"""
难度：中等

珂珂喜欢吃香蕉。这里有N堆香蕉，第i堆中有piles[i]根香蕉。警卫已经离开了，将在H小时后回来。 

珂珂可以决定她吃香蕉的速度K（单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉K根。
如果这堆香蕉少于K根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。
珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。 返回她可以在H小时内吃掉所有香蕉的最小速度K（K为整数）。 
示例 1： 
    输入: piles = [3,6,7,11], H = 8
    输出: 4

示例 2： 
    输入: piles = [30,11,23,4,20], H = 5
    输出: 30

示例 3： 
    输入: piles = [30,11,23,4,20], H = 6
    输出: 23

提示： 
    1 <= piles.length <= 10^4 
    piles.length <= H <= 10^9 
    1 <= piles[i] <= 10^9 

Related Topics 数组 二分查找
"""


class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def possible(k):
            return sum((p - 1) // k + 1 for p in piles) <= h

        left = 1
        right = max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if possible(mid):
                right = mid
            else:
                left = mid + 1
        return left


s = Solution()
# piles = [30, 11, 23, 4, 20]
# H = 5
# print(s.minEatingSpeed(piles, H))
#
# piles = [30, 11, 23, 4, 20]
# H = 6
# print(s.minEatingSpeed(piles, H))
#
piles = [312884470]
H = 968709470
print((312884470 + 968709470) // 2)
print(s.minEatingSpeed(piles, H))
