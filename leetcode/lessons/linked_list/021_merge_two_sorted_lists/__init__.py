#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project__ =  'leetcode'
__file__    =  '__init__.py.py'
__author__  =  'king'
__time__    =  '2019/11/15 10:48'


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

将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：
    输入：1->2->4, 1->3->4
    输出：1->1->2->3->4->4
'''


class Solution(object):
    @time_interval
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp = result = ListNode(0)
        while l1 and l2:
            if l1.val >= l2.val:
                temp.next = ListNode(l2.val)
                l2 = l2.next
            else:
                temp.next = ListNode(l1.val)
                l1 = l1.next
            temp = temp.next

        temp.next = l1 or l2

        return result.next


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(5)
l1.next = l2
l2.next = l3

l4 = ListNode(3)
l5 = ListNode(3)
l6 = ListNode(4)
l4.next = l5
l5.next = l6

print(Solution().mergeTwoLists(l1, l4))
