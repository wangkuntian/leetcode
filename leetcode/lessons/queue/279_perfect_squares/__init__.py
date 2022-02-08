#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project__ =  'leetcode'
__file__    =  '__init__.py.py'
__author__  =  'king'
__time__    =  '2020/2/22 18:40'


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

给定正整数n，找到若干个完全平方数（比如1, 4, 9, 16, ...）使得它们的和等于 n。
你需要让组成和的完全平方数的个数最少。

示例1:
输入: n = 12
输出: 3
解释: 12 = 4 + 4 + 4.

示例 2:
输入: n = 13
输出: 2
解释: 13 = 4 + 9.
"""


class Solution(object):

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [0, 1]
        while len(memo) <= n:
            memo.append(1 + min(memo[-i * i] for i in range(1, int(len(memo) ** 0.5) + 1)))

        return memo[n]

    def numSquares_2(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [i for i in range(n + 1)]

        for i in range(2, n + 1):
            for j in range(1, int(i ** 0.5) + 1):
                memo[i] = min(memo[i], memo[i - j * j] + 1)
        return memo[-1]

    def numSquares_3(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        四平方定理： 任何一个正整数都可以表示成不超过四个整数的平方之和。
        推论：满足四数平方和定理的数n（四个整数的情况），必定满足 n=(4^a)(8b+7)
        """
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4
        a = 0
        while a ** 2 <= n:
            b = int((n - a ** 2) ** 0.5)
            if a ** 2 + b ** 2 == n:
                return (not not a) + (not not b)
            a += 1
        return 3


# print(Solution().numSquares(13))
# print(Solution().numSquares_2(13))
print(Solution().numSquares_3(16))
