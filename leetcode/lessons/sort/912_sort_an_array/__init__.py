#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project__ =  'leetcode'
__file__    =  '__init__.py.py'
__author__  =  'king'
__time__    =  '2020/2/21 01:34'


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

给定一个整数数组nums，将该数组升序排列。

示例 1：
输入：[5,2,3,1]
输出：[1,2,3,5]

示例 2：
输入：[5,1,1,2,0,0]
输出：[0,0,1,1,2,5]

提示：
1 <= A.length <= 10000
-50000 <= A[i] <= 50000
"""


class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return sorted(nums)

    def quick_sort(self, nums, l, r):
        if l >= r:
            return
        left = l
        right = r
        pivot = nums[l]

        while left < right:
            while left < right and nums[right] >= pivot:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] <= pivot:
                left += 1
            nums[right] = nums[left]

        nums[left] = pivot
        self.quick_sort(nums, l, right - 1)
        self.quick_sort(nums, left + 1, r)


nums = [5, 4, 3, 2, 1]
print(Solution().sortArray(nums))
nums = [5, 4, 3, 2, 1]
Solution().quick_sort(nums, 0, len(nums) - 1)
print(nums)
