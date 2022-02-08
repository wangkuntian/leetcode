#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project__ =  'leetcode'
__file__    =  '__init__.py.py'
__author__  =  'king'
__time__    =  '2020/2/10 14:40'


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
难度：困难

给定两个大小为 m 和 n 的有序数组nums1 和nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为O(log(m + n))。

你可以假设nums1和nums2不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        def get_kth_smallest(a_start, b_start, k):
            if k <= 0 or k > len(nums1) - a_start + len(nums2) - b_start:
                raise ValueError('k is out of the bounds of the input lists')
            if a_start >= len(nums1):
                return nums2[b_start + k - 1]
            if b_start >= len(nums2):
                return nums1[a_start + k - 1]
            if k == 1:
                return min(nums1[a_start], nums2[b_start])

            mid_A = float('inf')
            mid_B = float('inf')

            if k // 2 - 1 < len(nums1) - a_start:
                mid_A = nums1[a_start + k // 2 - 1]
            if k // 2 - 1 < len(nums2) - b_start:
                mid_B = nums2[b_start + k // 2 - 1]

            if mid_A < mid_B:
                return get_kth_smallest(a_start + k // 2, b_start, k - k // 2)
            return get_kth_smallest(a_start, b_start + k // 2, k - k // 2)

        right = get_kth_smallest(0, 0, 1 + (len(nums1) + len(nums2)) // 2)
        if (len(nums1) + len(nums2)) % 2 == 1:
            return right
        left = get_kth_smallest(0, 0, (len(nums1) + len(nums2)) // 2)
        return (left + right) / 2.0


print(Solution().findMedianSortedArrays([1, 2], [3, 4]))
