#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project__ =  'leetcode'
__file__    =  '__init__.py.py'
__author__  =  'king'
__time__    =  '2019/11/18 11:50'


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
from leetcode.lessons.linked_list import ListNode
from leetcode.utils.timeutils import time_interval

'''
难度：简单

请判断一个链表是否为回文链表。

示例 1:
    输入: 1->2
    输出: false
    
示例 2:
    输入: 1->2->2->1
    输出: true
    
进阶：
    你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
'''


class Solution(object):
    @time_interval
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        x = None
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = x
            x = slow
            slow = temp

        if fast:
            slow = slow.next

        while slow:
            if slow.val != x.val:
                return False
            slow = slow.next
            x = x.next
        return True

    @time_interval
    def isPalindrome2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        x = []
        while head:
            x.append(head.val)
            head = head.next
        return x == x[::-1]


l1 = ListNode.generate([1, 2, 2, 1])
print(Solution().isPalindrome(l1))

l2 = ListNode.generate([1, 2, 2, 1])
print(Solution().isPalindrome2(l2))
