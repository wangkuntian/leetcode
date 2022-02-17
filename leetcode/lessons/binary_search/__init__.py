#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project__ =  'leetcode'
__file__    =  '__init__.py'
__author__  =  'king'
__time__    =  '2020/1/9 10:08'


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
二分查找也称折半查找（Binary Search），它是一种效率较高的查找方法，
前提是数据结构必须先排好序，可以在数据规模的对数时间复杂度内完成查找。
但是，二分查找要求线性表具有有随机访问的特点（例如数组），
也要求线性表能够根据中间元素的特点推测它两侧元素的性质，以达到缩减问题规模的效果。
"""


# 基本的二分搜索
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1

    return -1


# 1.寻找左侧边界的二分搜索
def left_bound(nums, target):
    if len(nums) == 0:
        return -1
    left = 0
    right = len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
    return left if nums[left] == target else -1


# 2.寻找左侧边界的二分搜索
def left_bound2(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    if nums[left] != target or left >= len(nums):
        return -1
    return left


# 1.寻找右侧边界的二分搜索
def right_bound(nums, target):
    if len(nums) == 0:
        return -1
    left = 0
    right = len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
    if right == 0 or nums[right - 1] != target:
        return -1
    return right - 1


# 2.寻找右侧边界的二分搜索
def right_bound(nums, target):
    if len(nums) == 0:
        return -1
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
    if right <= 0 or nums[right] != target:
        return -1
    return right


