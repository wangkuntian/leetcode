#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project__ =  'leetcode'
__file__    =  '__init__.py.py'
__author__  =  'king'
__time__    =  '2020/1/2 14:10'


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

给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。

示例:
输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出:  [1, 2, 4, 7, 5, 3, 6, 8, 9]

"""


class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        diagonal = []

        if not matrix or not matrix[0]:
            return diagonal

        rows = len(matrix)
        cols = len(matrix[0])

        up_right = True
        r = c = 0

        while len(diagonal) < rows * cols:
            diagonal.append(matrix[r][c])

            if up_right:
                if c == cols - 1:
                    r += 1
                    up_right = False
                elif r == 0:
                    c += 1
                    up_right = False
                else:
                    c += 1
                    r -= 1
            else:
                if r == rows - 1:
                    c += 1
                    up_right = True
                elif c == 0:
                    r += 1
                    up_right = True
                else:
                    r += 1
                    c -= 1
        return diagonal


print(
    Solution().findDiagonalOrder(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ])
)
