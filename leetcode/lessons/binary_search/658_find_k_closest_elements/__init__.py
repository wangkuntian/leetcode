#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project__ =  'leetcode'
__file__    =  '__init__.py.py'
__author__  =  'king'
__time__    =  '2020/1/9 17:34'


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

给定一个排序好的数组，两个整数 k 和 x，从数组中找到最靠近 x（两数之差最小）的 k 个数。
返回的结果必须要是按升序排好的。如果有两个数与 x 的差值一样，优先选择数值较小的那个数。

示例1:
输入: [1,2,3,4,5], k=4, x=3
输出: [1,2,3,4]

示例 2:
输入: [1,2,3,4,5], k=4, x=-1
输出: [1,2,3,4]

说明:
k 的值为正数，且总是小于给定排序数组的长度。
数组不为空，且长度不超过 10 ** 4
数组里的每个元素与x 的绝对值不超过 10 ** 4
"""


class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if x == arr[mid]:
                left = mid
                right = mid
                break
            elif x > arr[mid]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if right == len(arr) or abs(arr[left - 1] - x) <= abs(arr[right] - x):
                right = left
            else:
                left = right

        while right - left + 1 < k:
            if right + 1 == len(arr) or abs(arr[left - 1] - x) <= abs(arr[right + 1] - x):
                left -= 1
            else:
                right += 1

        return arr[left:right + 1]

    def findClosestElements_2(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        left = 0
        right = len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k]


print(Solution().findClosestElements([1, 2, 3, 4, 5], k=3, x=-1))
print(Solution().findClosestElements_2([1, 2, 3, 4, 5], k=3, x=5))
