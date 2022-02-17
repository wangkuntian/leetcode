#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project__ =  'leetcode'
__file__    =  '__init__.py'
__author__  =  'king'
__time__    =  '2019/11/18 15:05'


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

给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中没有重复出现的数字。

示例1:
    输入: 1->2->3->3->4->4->5
    输出: 1->2->5

示例2:
    输入: 1->1->1->2->3
    输出: 2->3
'''


class Solution(object):
    @time_interval
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        result = temp = ListNode(None)
        result.next = head
        node = head
        while node:
            if node.next and node.val == node.next.val:
                value = node.val
                node = node.next
                while node and node.val == value:
                    node = node.next
                temp.next = None
            else:
                temp.next = node
                temp = node
                node = node.next
        return result.next

    @time_interval
    def deleteDuplicates2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        result = temp = ListNode(None)
        result.next = head
        while temp.next and temp.next.next:
            x = temp.next
            y = temp.next.next
            if x.val == y.val:
                while x.val == y.val:
                    y = y.next
                    if not y:
                        break
                temp.next = y
            else:
                temp = x
        return result.next


l1 = ListNode.generate([1, 1, 1, 2, 3, 4, 4])
print(Solution().deleteDuplicates(l1))

l2 = ListNode.generate([1, 1, 1, 2, 3, 4, 4])
print(Solution().deleteDuplicates2(l2))
