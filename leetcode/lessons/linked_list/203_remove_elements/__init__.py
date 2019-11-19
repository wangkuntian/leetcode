#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project__ =  'leetcode'
__file__    =  '__init__.py.py'
__author__  =  'king'
__time__    =  '2019/11/15 17:55'


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

删除链表中等于给定值 val 的所有节点。

示例:
    输入: 1->2->6->3->4->5->6, val = 6
    输出: 1->2->3->4->5
'''


class Solution(object):
    @time_interval
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        temp = result = ListNode(None)
        result.next = head
        while temp.next:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next

        return result.next


l1 = ListNode.generate([1, 1, 1])

print(Solution().removeElements(l1, 1))
