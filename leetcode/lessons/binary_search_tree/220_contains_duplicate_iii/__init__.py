#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project__ =  'leetcode'
__file__    =  '__init__.py'
__author__  =  'king'
__time__    =  '2020/2/18 10:43'


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

"""
难度：中等

给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j，
使得nums [i] 和nums [j]的差的绝对值最大为 t，并且 i 和 j 之间的差的绝对值最大为 ķ。

示例1:
输入: nums = [1,2,3,1], k = 3, t = 0
输出: true

示例 2:
输入: nums = [1,0,1,1], k = 1, t = 2
输出: true

示例 3:
输入: nums = [1,5,9,1,5,9], k = 2, t = 3
输出: false
"""

from leetcode.lessons.binary_search_tree import TreeNode


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0 or k < 0:
            return False
        buckets = {}
        # 桶的大小设成t+1更加方便
        bucket_size = t + 1
        for i in range(len(nums)):
            # 放入哪个桶
            num = nums[i] // bucket_size

            # 桶中已经有元素了
            if num in buckets:
                return True

            # 把nums[i]放入桶中
            buckets[num] = nums[i]

            # 检查前一个桶
            if (num - 1) in buckets and abs(buckets[num - 1] - nums[i]) <= t:
                return True
            # 检查后一个桶
            if (num + 1) in buckets and abs(buckets[num + 1] - nums[i]) <= t:
                return True

            if i >= k:
                buckets.pop(nums[i - k] // bucket_size)

        return False


print(Solution().containsNearbyAlmostDuplicate(nums=[1, 2, 3, 1], k=3, t=0))
print(Solution().containsNearbyAlmostDuplicate(nums=[1, 0, 1, 1], k=1, t=2))
print(Solution().containsNearbyAlmostDuplicate(nums=[1, 5, 9, 1, 5, 9], k=2, t=3))
print(Solution().containsNearbyAlmostDuplicate(nums=[7, 1, 3], k=2, t=3))
