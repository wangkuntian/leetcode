#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project__ =  'leetcode'
__file__    =  '__init__.py.py'
__author__  =  'king'
__time__    =  '2020/2/20 16:43'


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

给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。
一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。
你可以假设网格的四个边均被水包围。

示例 1:
输入:
11110
11010
11000
00000
输出: 1

示例 2:
输入:
11000
11000
00100
00011

输出: 3
"""

import collections


class Solution(object):
    # DFS
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    print(r, c)
                    self.set_island(r, c, grid)
                    print(r, c)

        return islands

    def set_island(self, row, col, grid):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return
        if grid[row][col] != '1':
            return
        grid[row][col] = '0'
        self.set_island(row + 1, col, grid)
        self.set_island(row - 1, col, grid)
        self.set_island(row, col + 1, grid)
        self.set_island(row, col - 1, grid)

    # BFS
    def numIslands_2(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    grid[r][c] = '0'
                    queue = collections.deque([(r, c)])
                    while queue:
                        row, col = queue.popleft()
                        if row - 1 >= 0 and grid[row - 1][col] == '1':
                            queue.append((row - 1, col))
                            grid[row - 1][col] = '0'
                        if row + 1 < rows and grid[row + 1][col] == '1':
                            queue.append((row + 1, col))
                            grid[row + 1][col] = '0'
                        if col - 1 >= 0 and grid[row][col - 1] == '1':
                            queue.append((row, col - 1))
                            grid[row][col - 1] = '0'
                        if col + 1 < cols and grid[row][col + 1] == '1':
                            queue.append((row, col + 1))
                            grid[row][col + 1] = '0'
        return islands


nums = [['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']]
print(Solution().numIslands_2(
    nums
))
print(nums)

print(Solution().numIslands(
    nums
))
print(nums)

print(Solution().numIslands(
    [["1", "1", "1", "1", "0"],
     ["1", "1", "0", "1", "0"],
     ["1", "1", "0", "0", "0"],
     ["0", "0", "0", "0", "0"]]
))
