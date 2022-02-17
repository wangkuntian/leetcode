# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project__ =  'leetcode'
__file__    =  '__init__.py.py'
__author__  =  'king'
__time__    =  '2022/2/14 20:45'


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
import string

"""
难度：困难

给你一个字符串s、一个字符串t。返回s中涵盖t所有字符的最小子串。如果s中不存在涵盖t所有字符的子串，
则返回空字符串 "" 。 

注意： 
    对于t中重复字符，我们寻找的子字符串中该字符数量必须不少于t中该字符数量。 
    如果s中存在这样的子串，我们保证它是唯一的答案。 

示例 1： 
    输入：s = "ADOBECODEBANC", t = "ABC"
    输出："BANC"

示例 2： 
    输入：s = "a", t = "a"
    输出："a"

示例 3: 
    输入: s = "a", t = "aa"
    输出: ""
    
    解释: t 中两个字符 'a' 均应包含在 s 的子串中，
    因此没有符合条件的子字符串，返回空字符串。 

提示： 
    1 <= s.length, t.length <= 10⁵ 
    s 和 t 由英文字母组成 
进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？ 

Related Topics 哈希表 字符串 滑动窗口
"""
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.defaultdict(int)
        window = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        left = right = 0
        valid = 0
        start = 0
        length = max_length = float('inf')
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            while valid == len(need):
                if right - left < length:
                    start = left
                    length = right - left
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return "" if length == max_length else s[start: start + length]


s = "ADOBECODEBANC"
t = "ABC"
ss = Solution()
# print(ss.minWindow(s, t))

s = "a"
t = "aa"
print(ss.minWindow(s, t))
