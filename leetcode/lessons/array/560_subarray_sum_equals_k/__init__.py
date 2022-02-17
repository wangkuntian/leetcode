# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project__ =  'leetcode'
__file__    =  '__init__.py.py'
__author__  =  'king'
__time__    =  '2022/2/14 18:12'


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

给你一个整数数组nums和一个整数k ，请你统计并返回该数组中和为k的连续子数组的个数。

示例 1：
    输入：nums = [1,1,1], k = 2
    输出：2

示例 2：
    输入：nums = [1,2,3], k = 3
    输出：2

提示：
    1 <= nums.length <= 2 * 10⁴
    -1000 <= nums[i] <= 1000
    -10⁷ <= k <= 10⁷

Related Topics 数组 哈希表 前缀和
"""
import collections


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        pre_sum = collections.defaultdict(int)
        current_sum = 0
        for num in nums:
            current_sum += num
            if current_sum == k:
                total += 1
            if current_sum - k in pre_sum:
                total += pre_sum[current_sum - k]
            pre_sum[current_sum] += 1
        return total

    def subarraySum2(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        pre_sum = [0] * (n + 1)
        for i in range(n):
            pre_sum[i + 1] = nums[i] + pre_sum[i]
        for i in range(1, n + 1):
            for j in range(i):
                if pre_sum[i] - pre_sum[j] == k:
                    count += 1
        return count


s = Solution().subarraySum([3, 5, 2, -2, 4, 1], 5)
print(s)
