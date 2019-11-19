#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project__ =  'leetcode'
__file__    =  '__init__.py.py'
__author__  =  'king'
__time__    =  '2019/11/18 10:08'


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

编写一个程序，找到两个单链表相交的起始节点。
'''

import gc


class Solution(object):
    @time_interval
    def getIntersectionNode(self, headA, headB):
        """
        :type: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        x = headA
        y = headB
        while headA != headB:
            headA = y if not headA else headA.next
            headB = x if not headB else headB.next
        gc.collect()
        return headA


l1 = ListNode(4)
l2 = ListNode(1)
l3 = ListNode(8)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

l6 = ListNode(5)
l7 = ListNode(0)
l8 = ListNode(1)
l6.next = l7
l7.next = l8
l8.next = l3

print(Solution().getIntersectionNode(l1, l6))
