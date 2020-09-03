#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project__ =  'leetcode'
__file__    =  '__init__.py.py'
__author__  =  'king'
__time__    =  '2020/3/2 15:51'


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

给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。

两个相邻元素间的距离为 1 。

示例 1:
输入:

0 0 0
0 1 0
0 0 0
输出:

0 0 0
0 1 0
0 0 0
示例 2:
输入:

0 0 0
0 1 0
1 1 1
输出:

0 0 0
0 1 0
1 2 1
注意:

给定矩阵的元素个数不超过 10000。
给定矩阵中至少有一个元素是 0。
矩阵中的元素只在四个方向上相邻: 上、下、左、右。
"""
import collections


class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(matrix)
        cols = len(matrix[0])
        deltas = [
            (1, 0), (-1, 0),
            (0, 1), (0, -1)
        ]
        queue = collections.deque()
        max_dist = rows + cols - 1

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 1:
                    matrix[r][c] = max_dist
                else:
                    queue.append((r, c))
        print(matrix)
        while queue:
            print('before', queue)
            r, c = queue.popleft()
            for dr, dc in deltas:
                if 0 <= r + dr < rows and 0 <= c + dc < cols and matrix[r][c] + 1 < matrix[r + dr][c + dc]:
                    matrix[r + dr][c + dc] = matrix[r][c] + 1
                    queue.append((r + dr, c + dc))
            print('after', queue)
        return matrix

    def updateMatrix2(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        deltas = [
            (1, 0), (-1, 0),
            (0, 1), (0, -1)
        ]
        unknown = set()
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 1:
                    unknown.add((r, c))
        while unknown:
            new_unknown = set()
            for r, c in unknown:
                for dr, dc in deltas:
                    if 0 <= r + dr < rows and 0 <= c + dc < cols and (r + dr, c + dc) not in unknown:
                        matrix[r][c] = matrix[r + dr][c + dc] + 1
                        break
                else:
                    new_unknown.add((r, c))
            unknown = new_unknown
        return matrix


matrix = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 0]
]
print(Solution().updateMatrix(matrix))
matrix = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 0]
]
print(Solution().updateMatrix2(matrix))
