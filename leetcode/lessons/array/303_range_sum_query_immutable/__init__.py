# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project__ =  'leetcode'
__file__    =  '__init__.py.py'
__author__  =  'king'
__time__    =  '2022/2/14 15:45'


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
难度：简单

给定一个整数数组 nums，处理以下类型的多个查询:

计算索引left和right（包含 left 和 right）之间的nums元素的和，其中left <= right

实现 NumArray 类：
NumArray(int[] nums) 使用数组nums初始化对象
int sumRange(int i, int j) 返回数组 nums 中索引left和right之间的元素的总和，
包含left和right两点（也就是 nums[left] + nums[left + 1] + ... + nums[right] )

示例 1：
    输入：
    ["NumArray", "sumRange", "sumRange", "sumRange"]
    [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]

    输出：
    [null, 1, -1, -3]

    解释：
    NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
    numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
    numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1))
    numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))

提示：
    0 <= nums.length <= 10⁴
    -10⁵ <= nums[i] <= 10⁵
    0 <= i <= j < nums.length
    最多调用 10⁴ 次 sumRange 方法

Related Topics 设计 数组 前缀和

"""


class NumArray:

    def __init__(self, nums: List[int]):
        self.pre_sum = [0]
        for num in nums:
            self.pre_sum.append(self.pre_sum[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.pre_sum[right + 1] - self.pre_sum[left]

