#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project__ =  'leetcode'
__file__    =  '__init__.py.py'
__author__  =  'king'
__time__    =  '2020/3/3 09:52'


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

给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。
编写一个方法，将 B 合并入 A 并排序。

初始化 A 和 B 的元素数量分别为 m 和 n。

示例:

输入:
A = [1,2,3,0,0,0], m = 3
B = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]
"""


class Solution(object):
    def merge(self, A, m, B, n):
        """
        :type A: List[int]
        :type m: int
        :type B: List[int]
        :type n: int
        :rtype: None Do not return anything, modify A in-place instead.
        """
        l = []
        a = 0
        b = 0
        while a < m or b < n:
            if a == m:
                l.append(B[b])
                b += 1
            elif b == n:
                l.append(A[a])
                a += 1
            elif A[a] < B[b]:
                l.append(A[a])
                a += 1
            elif A[a] >= B[b]:
                l.append(B[b])
                b += 1

        A[:] = l

    def merge_2(self, A, m, B, n):
        """
        :type A: List[int]
        :type m: int
        :type B: List[int]
        :type n: int
        :rtype: None Do not return anything, modify A in-place instead.
        """
        a = 0
        b = 0
        l = []
        while a < m and b < n:
            if A[a] > B[b]:
                l.append(B[b])
                b += 1
            else:
                l.append(A[a])
                a += 1
        if a < m:
            l += A[a:m]
        else:
            l += B[b:n]

        A[:] = l

    def merge_3(self, A, m, B, n):
        """
        :type A: List[int]
        :type m: int
        :type B: List[int]
        :type n: int
        :rtype: None Do not return anything, modify A in-place instead.
        """
        a = m - 1
        b = n - 1
        k = m + n - 1

        while a >= 0 and b >= 0:
            if A[a] > B[b]:
                A[k] = A[a]
                a -= 1
            else:
                A[k] = B[b]
                b -= 1
            k -= 1
        print(A)
        if a < 0:
            A[:k + 1] = B[: b + 1]


A = [4, 5, 6, 7, 0, 0, 0]
m = 4
B = [1, 5, 6]
n = 3
Solution().merge_3(A, m, B, n)
print(A)
