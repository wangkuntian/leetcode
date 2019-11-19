#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project__ =  'leetcode'
__file__    =  '__init__.py.py'
__author__  =  'king'
__time__    =  '2019/11/15 14:04'


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
难度：中等

给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例:
    给定 1->2->3->4, 你应该返回 2->1->4->3.

'''


class Solution(object):
    @time_interval
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        temp = head.next
        head.next = self.swapPairs(temp.next)
        temp.next = head
        return temp

    @time_interval
    def swapPairs2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        result = ListNode(-1)
        result.next = head
        x = result
        while x.next and x.next.next:
            a, b = x.next, x.next.next
            a.next = b.next
            b.next = a
            x.next = b
            x = x.next.next
        return result.next


l1 = ListNode.generate(nums=[1, 2, 3, 4])

print(Solution().swapPairs(l1))

l2 = ListNode.generate(nums=[1, 2, 3, 4])

print(Solution().swapPairs2(l2))
