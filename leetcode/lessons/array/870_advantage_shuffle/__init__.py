# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project__ =  'leetcode'
__file__    =  '__init__.py.py'
__author__  =  'king'
__time__    =  '2022/2/16 15:30'


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

给定两个大小相等的数组A和B，A相对于B的优势可以用满足A[i] > B[i]的索引i的数目来描述。 
返回A的任意排列，使其相对于B的优势最大化。 

示例 1： 
    输入：A = [2,7,11,15], B = [1,10,4,11]
    输出：[2,11,7,15]

示例 2： 
    输入：A = [12,24,8,32], B = [13,25,32,11]
    输出：[24,32,8,12]

提示： 
    1 <= A.length = B.length <= 10000 
    0 <= A[i] <= 10^9 
    0 <= B[i] <= 10^9 

Related Topics 贪心 数组 排序
"""


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums = sorted([(b, i) for i, b in enumerate(nums2)],
                      key=lambda x: x[0])
        result = [0] * len(nums1)
        i = 0
        for a in sorted(nums1):
            if a > nums[i][0]:
                result[nums[i][1]] = a
                i += 1
            else:
                result[nums.pop()[1]] = a
        return result


s = Solution()

A = [2, 7, 11, 15]
B = [1, 10, 4, 11]
print(s.advantageCount(A, B))

A = [2, 0, 4, 1, 2]
B = [1, 3, 0, 0, 2]
print(s.advantageCount(A, B))