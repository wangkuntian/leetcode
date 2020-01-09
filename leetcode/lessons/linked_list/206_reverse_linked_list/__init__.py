#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project__ =  'leetcode'
__file__    =  '__init__.py.py'
__author__  =  'king'
__time__    =  '2019/11/15 17:11'


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

反转一个单链表。

示例:
    输入: 1->2->3->4->5->NULL
    输出: 5->4->3->2->1->NULL
进阶:
    你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
'''


class Solution(object):
    @time_interval
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        x = None
        while head:
            temp = head.next
            head.next = x
            x = head
            head = temp
        return x

    @time_interval
    def reverseList_2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        result = self.reverseList_2(head.next)
        head.next.next = head
        head.next = None
        return result


l1 = ListNode.generate([1, 2, 3, 4, 5])
print(Solution().reverseList(l1))

l2 = ListNode.generate([1, 2, 3, 4, 5])
print(Solution().reverseList_2(l2))
