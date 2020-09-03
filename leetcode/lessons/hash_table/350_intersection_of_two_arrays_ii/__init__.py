#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project__ =  'leetcode'
__file__    =  '__init__.py.py'
__author__  =  'king'
__time__    =  '2020/7/13 16:39'


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
给定两个数组，编写一个函数来计算它们的交集。

示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]

示例 2:
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]

说明：
输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
我们可以不考虑输出结果的顺序。

进阶：
如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
"""
from leetcode.utils.timeutils import time_interval
from collections import Counter


class Solution(object):
    @time_interval
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()

        result = []

        length_1 = len(nums1)
        length_2 = len(nums2)

        index_1 = index_2 = 0

        while index_1 < length_1 and index_2 < length_2:
            if nums1[index_1] > nums2[index_2]:
                index_2 += 1
            elif nums1[index_1] < nums2[index_2]:
                index_1 += 1
            else:
                result.append(nums1[index_1])
                index_1 += 1
                index_2 += 1
        return result

    @time_interval
    def intersection_2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        counter = Counter(nums1)

        result = []

        for index, num in enumerate(nums2):
            if num in counter and counter[num] > 0:
                counter[num] -= 1
                result.append(num)
        return result

    @time_interval
    def intersection_3(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        counter = Counter(nums1)

        result = []

        for index, num in enumerate(nums2):
            if num in counter and counter[num] > 0:
                counter[num] -= 1
                result.append(num)
        return result


s = Solution()
l1 = [1, 2, 2, 1]
l2 = [2, 2]
print(s.intersection(l1, l2))
l1 = [1, 2, 2, 1]
l2 = [2, 2]
print(s.intersection_2(l1, l2))
l1 = [1, 2, 2, 1]
l2 = [2, 2]
print(s.intersection_3(l1, l2))
