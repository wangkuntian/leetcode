# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project__ =  'leetcode'
__file__    =  '__init__.py.py'
__author__  =  'king'
__time__    =  '2022/2/14 19:58'


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

这里有n个航班，它们分别从1到n进行编号。 
有一份航班预订表bookings ，表中第i条预订记录
bookings[i] = [firsti, lasti, seatsi]意味着在从firsti到lasti(包含firsti和lasti）
的每个航班上预订了seatsi个座位。 

请你返回一个长度为n的数组answer，里面的元素是每个航班预定的座位总数。 

示例 1： 
    输入：bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
    输出：[10,55,45,25,25]
    
    解释：
    航班编号        1   2   3   4   5
    预订记录 1 ：   10  10
    预订记录 2 ：       20  20
    预订记录 3 ：       25  25  25  25
    总座位数：      10  55  45  25  25
    因此，answer = [10,55,45,25,25]


示例 2： 
    输入：bookings = [[1,2,10],[2,2,15]], n = 2
    输出：[10,25]
    
    解释：
    航班编号        1   2
    预订记录 1 ：   10  10
    预订记录 2 ：       15
    总座位数：      10  25
    因此，answer = [10,25]

提示： 
    1 <= n <= 2 * 10⁴ 
    1 <= bookings.length <= 2 * 10⁴ 
    bookings[i].length == 3 
    1 <= firsti <= lasti <= n 
    1 <= seatsi <= 10⁴ 

Related Topics 数组 差分数组
"""


class Solution:
    def corpFlightBookings(
            self, bookings: List[List[int]], n: int) -> List[int]:
        result = [0] * (n + 1)
        for i, j, inc in bookings:
            result[i - 1] += inc
            result[j] -= inc
        for i in range(1, n + 1):
            result[i] += result[i - 1]
        return result[:-1]


bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
n = 5
s = Solution()
print(s.corpFlightBookings(bookings, n))
