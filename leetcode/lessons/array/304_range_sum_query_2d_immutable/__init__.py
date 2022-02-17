# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project__ =  'leetcode'
__file__    =  '__init__.py.py'
__author__  =  'king'
__time__    =  '2022/2/14 16:01'


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
from typing import List

"""
难度：中等

给定一个二维矩阵 matrix，以下类型的多个请求：
计算其子矩形范围内元素的总和，该子矩阵的左上角为(row1, col1) ，右下角为(row2, col2) 。

实现 NumMatrix 类：NumMatrix(int[][] matrix) 给定整数矩阵 matrix 进行初始化
int sumRegion(int row1, int col1, int row2, int col2) 返回
左上角 (row1, col1) 、右下角 (row2, col2) 所描述的子矩阵的元素总和 。

示例 1：
    输入:
    ["NumMatrix","sumRegion","sumRegion","sumRegion"]
    [[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,
    1,2,2],[1,2,2,4]]
    输出:
    [null, 8, 11, 12]
    解释:
    NumMatrix numMatrix = new NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,
    0,1,7],[1,0,3,0,5]]);
    numMatrix.sumRegion(2, 1, 4, 3); // return 8 (红色矩形框的元素总和)
    numMatrix.sumRegion(1, 1, 2, 2); // return 11 (绿色矩形框的元素总和)
    numMatrix.sumRegion(1, 2, 2, 4); // return 12 (蓝色矩形框的元素总和)

提示：
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 200
    -10⁵ <= matrix[i][j] <= 10⁵
    0 <= row1 <= row2 < m
    0 <= col1 <= col2 < n
    最多调用 10⁴ 次 sumRegion 方法

Related Topics 设计 数组 矩阵 前缀和

"""


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return

        rows = len(matrix)
        cols = len(matrix[0])

        self.pre_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                self.pre_sum[r][c] = (self.pre_sum[r - 1][c] +
                                      self.pre_sum[r][c - 1] +
                                      matrix[r - 1][c - 1] -
                                      self.pre_sum[r - 1][c - 1])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.pre_sum[row2 + 1][col2 + 1] -
                self.pre_sum[row1][col2 + 1] -
                self.pre_sum[row2 + 1][col1] +
                self.pre_sum[row1][col1])


class NumMatrix2:
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return

        rows, cols = len(matrix), len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                if c != 0:
                    matrix[r][c] += matrix[r][c - 1]
                if r != 0:
                    matrix[r][c] += matrix[r - 1][c]
                if c != 0 and r != 0:
                    matrix[r][c] -= matrix[r - 1][c - 1]

        self.matrix = matrix

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        region = self.matrix[row2][col2]
        if col1 != 0:
            region -= self.matrix[row2][col1 - 1]
        if row1 != 0:
            region -= self.matrix[row1 - 1][col2]
        if row1 != 0 and col1 != 0:
            region += self.matrix[row1 - 1][col1 - 1]
        return region


m = [[3, 0, 1, 4, 2],
     [5, 6, 3, 2, 1],
     [1, 2, 0, 1, 5],
     [4, 1, 0, 1, 7],
     [1, 0, 3, 0, 5]]
x1, x2, y1, y2 = (1, 2, 2, 4)

s = NumMatrix(matrix=m)
print(s.sumRegion(x1, x2, y1, y2))
s = NumMatrix2(matrix=m)
print(s.sumRegion(x1, x2, y1, y2))

mm = [[-4, -5]]
s = NumMatrix(matrix=mm)
print(s.sumRegion(0, 0, 0, 0))
