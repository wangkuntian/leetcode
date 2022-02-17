# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project__ =  'leetcode'
__file__    =  '__init__.py.py'
__author__  =  'king'
__time__    =  '2022/2/15 16:28'


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

给定两个字符串s和p，找到s中所有p的异位词的子串，返回这些子串的起始索引。不考虑答案输出的顺序。 
异位词指由相同字母重排列形成的字符串（包括相同的字符串）。 

示例 1: 
    输入: s = "cbaebabacd", p = "abc"
    输出: [0,6]
    解释:
    起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
    起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。

示例 2: 
    输入: s = "abab", p = "ab"
    输出: [0,1,2]
    解释:
    起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
    起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
    起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。

提示: 
    1 <= s.length, p.length <= 3 * 10⁴ 
    s 和 p 仅包含小写字母 

Related Topics 哈希表 字符串 滑动窗口
"""

import collections


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window = collections.defaultdict(int)
        needs = collections.defaultdict(int)
        for c in p:
            needs[c] += 1
        result = []
        left = right = valid = 0
        while right < len(s):
            c = s[right]
            right += 1
            if c in needs:
                window[c] += 1
                if window[c] == needs[c]:
                    valid += 1
            while right - left >= len(p):

                if valid == len(needs):
                    result.append(left)
                d = s[left]
                left += 1
                if d in needs:
                    if window[d] == needs[d]:
                        valid -= 1
                    window[d] -= 1
        return result


s = "cbaebabacd"
p = "abc"
ss = Solution()
print(ss.findAnagrams(s, p))
s = "abab"
p = "ab"
print(ss.findAnagrams(s, p))
