# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project__ =  'leetcode'
__file__    =  '__init__.py.py'
__author__  =  'king'
__time__    =  '2022/2/16 14:47'


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

传送带上的包裹必须在days天内从一个港口运送到另一个港口。 

传送带上的第i个包裹的重量为weights[i]。每一天，我们都会按给出重量（weights）的顺序往传送带上装载包裹。
我们装载的重量不会超过船的最大运载重量。 返回能在days天内将传送带上的所有包裹送达的船的最低运载能力。 

示例 1： 
    输入：weights = [1,2,3,4,5,6,7,8,9,10], days = 5
    输出：15
    解释：
    船舶最低载重 15 就能够在 5 天内送达所有包裹，如下所示：
    第 1 天：1, 2, 3, 4, 5
    第 2 天：6, 7
    第 3 天：8
    第 4 天：9
    第 5 天：10

请注意，货物必须按照给定的顺序装运，
因此使用载重能力为14的船舶并将包装分成 (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) 是不允许的。 

示例 2： 
    输入：weights = [3,2,2,4,1,4], days = 3
    输出：6
    解释：
    船舶最低载重 6 就能够在 3 天内送达所有包裹，如下所示：
    第 1 天：3, 2
    第 2 天：2, 4
    第 3 天：1, 4


示例 3： 
    输入：weights = [1,2,3,1,1], D = 4
    输出：3
    解释：
    第 1 天：1
    第 2 天：2
    第 3 天：3
    第 4 天：1, 1

提示： 
    1 <= days <= weights.length <= 5 * 10⁴ 
    1 <= weights[i] <= 500 

Related Topics 贪心 数组 二分查找
"""


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = (left + right) // 2
            need, cur = 1, 0
            for w in weights:
                if cur + w > mid:
                    need += 1
                    cur = 0
                cur += w
            if need <= days:
                right = mid
            else:
                left = mid + 1
        return left


s = Solution()

weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5
print(s.shipWithinDays(weights, days))
