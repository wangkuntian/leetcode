# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project__ =  'leetcode'
__file__    =  '__init__.py.py'
__author__  =  'king'
__time__    =  '2022/2/15 16:02'


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

给你两个字符串s1和s2，写一个函数来判断s2是否包含s1的排列。如果是，返回true；否则，返回false。 

换句话说，s1的排列之一是s2的子串。
 
示例 1： 
    输入：s1 = "ab" s2 = "eidbaooo"
    输出：true
    
    解释：s2 包含 s1 的排列之一 ("ba").

示例 2： 
    输入：s1= "ab" s2 = "eidboaoo"
    输出：false

提示： 
    1 <= s1.length, s2.length <= 10⁴ 
    s1 和 s2 仅包含小写字母 

Related Topics 哈希表 双指针 字符串 滑动窗口
"""
import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = collections.defaultdict(int)
        needs = collections.defaultdict(int)

        for c in s1:
            needs[c] += 1
        left = right = valid = 0
        while right < len(s2):
            c = s2[right]
            right += 1
            if c in needs:
                window[c] += 1
                if needs[c] == window[c]:
                    valid += 1

            while right - left >= len(s1):
                if valid == len(s1):
                    return True
                d = s2[left]
                left += 1
                if d in needs:
                    if window[d] == needs[d]:
                        valid -= 1
                    window[d] -= 1
        return False


s1 = "ab"
s2 = "eidbaooo"
s = Solution()
print(s.checkInclusion(s1, s2))
s1 = "ab"
s2 = "eidboaoo"
print(s.checkInclusion(s1, s2))
