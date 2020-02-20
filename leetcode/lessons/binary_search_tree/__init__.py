#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project__ =  'leetcode'
__file__    =  '__init__.py.py'
__author__  =  'king'
__time__    =  '2020/2/13 20:33'


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

二叉搜索树（BST）是二叉树的一种特殊表示形式，它满足如下特性：

每个节点中的值必须大于（或等于）存储在其左侧子树中的任何值。
每个节点中的值必须小于（或等于）存储在其右子树中的任何值。

如：
      5
    /   \
   2     6
 /   \    \
1     4    7
    /
   3

对于二叉搜索树，可以通过中序遍历得到一个递增的有序序列。
"""

from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        # 输出前序遍历
        nodes = []

        def preorder(node):
            if not node:
                nodes.append('None')
            else:
                nodes.append(str(node.val))
                preorder(node.left)
                preorder(node.right)

        preorder(self)
        return ', '.join(nodes)

    @classmethod
    def generate(cls, nums):
        """
        :param nums: 前序遍历
        :type nums: list
        :rtype: TreeNode
        """
        nodes = deque(nums)

        def build():
            if not nodes:
                return None
            node = nodes.popleft()
            if node is None:
                return None
            node = TreeNode(node)
            node.left = build()
            node.right = build()
            return node

        return build()
