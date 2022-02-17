# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project__ =  'leetcode'
__file__    =  '__init__.py'
__author__  =  'king'
__time__    =  '2022/2/14 10:13'


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

给你一个字符串s，找到s中最长的回文子串。
示例 1：
    输入：s = "babad"
    输出："bab"
    解释："aba" 同样是符合题意的答案。

示例 2：
    输入：s = "cbbd"
    输出："bb"

示例 3：
    输入：s = "a"
    输出："a"

示例 4：
    输入：s = "ac"
    输出："a"

提示：
    1 <= s.length <= 1000
    s 仅由数字和英文字母（大写和/或小写）组成

Related Topics 字符串 动态规划
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        res = s[:1]
        for i in range(len(s)):
            palindrome_odd = self.spread(s, i, i)
            palindrome_even = self.spread(s, i, i + 1)
            # 当前找到的最长回文子串
            res = max(palindrome_odd, palindrome_even, res, key=len)
        return res

    @staticmethod
    def spread(s, left, right):
        """
        left = right 的时候，此时回文中心是一条线，回文串的长度是奇数
        right = left + 1 的时候，此时回文中心是任意一个字符，回文串的长度是偶数
        """

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
