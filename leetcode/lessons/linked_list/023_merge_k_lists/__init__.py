#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project__ =  'leetcode'
__file__    =  '__init__.py'
__author__  =  'king'
__time__    =  '2019/11/15 11:27'


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
import heapq
from leetcode.lessons.linked_list import ListNode
from leetcode.utils.timeutils import time_interval

'''
难度：困难

合并k个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:
    输入:
    [
     1->4->5,
     1->3->4,
     2->6
    ]
    输出: 1->1->2->3->4->4->5->6
'''


class Solution(object):
    @time_interval
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        temp = result = ListNode(0)
        nodes = [(l.val, l) for l in lists if l]
        heapq.heapify(nodes)

        while nodes:
            value, node = heapq.heappop(nodes)
            temp.next = node
            temp = temp.next
            if node.next:
                heapq.heappush(nodes, (node.next.val, node.next))

        return result.next


l1 = ListNode.generate([1, 2, 5])

l4 = ListNode.generate([3, 3, 4])

print(Solution().mergeKLists([l1, l4]))
