#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__project__ =  'leetcode'
__file__    =  '__init__.py.py'
__author__  =  'king'
__time__    =  '2019/11/18 16:54'


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
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
    1 ≤ m ≤ n ≤ 链表长度。

示例:
    输入: 1->2->3->4->5->NULL, m = 2, n = 4
    输出: 1->4->3->2->5->NULL
'''


class Solution(object):
    @time_interval
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        result = node = ListNode(None)
        result.next = head
        n -= m
        while m > 1:
            node = node.next
            m -= 1
        tail = None
        reversed_head = None
        next_reverse = node.next

        while n >= 0:
            tail = next_reverse.next
            next_reverse.next = reversed_head
            reversed_head = next_reverse
            next_reverse = tail
            n -= 1
        node.next.next = tail
        node.next = reversed_head

        return result.next

    @time_interval
    def reverseBetween2(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None

        cur, pre = head, None

        while m > 1:
            pre = cur
            cur = cur.next
            m -= 1
            n -= 1

        tail, con = cur, pre
        while n:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
            n -= 1
        if con:
            con.next = pre
        else:
            head = pre

        tail.next = cur
        return head


l1 = ListNode.generate([1, 2, 3, 4, 5])
print(Solution().reverseBetween(l1, 2, 4))

l2 = ListNode.generate([1, 2, 3, 4, 5])
print(Solution().reverseBetween2(l2, 2, 4))
