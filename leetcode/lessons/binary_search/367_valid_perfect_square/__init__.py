#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project__ =  'leetcode'
__file__    =  '__init__.py'
__author__  =  'king'
__time__    =  '2020/1/10 20:39'


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
难度：简单

给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

说明：不要使用任何内置的库函数，如sqrt。

示例 1：
输入：16
输出：True

示例 2：
输入：14
输出：False
"""


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return True

        left = 2
        right = num // 2

        while left <= right:
            mid = (left + right) // 2
            result = mid * mid
            if result == num:
                return True
            elif result > num:
                right = mid - 1
            elif result < num:
                left = mid + 1
        return False

    def isPerfectSquare_2(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return True

        left = 2
        right = num

        while left < right:
            mid = (left + right) // 2
            result = mid * mid
            if result == num:
                return True
            elif result > num:
                right = mid
            elif result < num:
                left = mid + 1
        return False


print(Solution().isPerfectSquare(0))
print(Solution().isPerfectSquare_2(16))

