#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project__ =  'leetcode'
__file__    =  '__init__.py.py'
__author__  =  'king'
__time__    =  '2020/2/10 15:34'


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
树是一种经常用到的数据结构，用来模拟具有树状结构性质的数据集合。

树里的每一个节点有一个根植和一个包含所有子节点的列表。
从图的观点来看，树也可视为一个拥有N个节点和N-1条边的一个有向无环图。

二叉树是一种更为典型的树树状结构。
如它名字所描述的那样，二叉树是每个节点最多有两个子树的树结构，通常子树被称作“左子树”和“右子树”。
"""

"""
前序遍历
前序遍历首先访问根节点，然后遍历左子树，最后遍历右子树。

中序遍历
中序遍历是先遍历左子树，然后访问根节点，然后遍历右子树。

后序遍历
后序遍历是先遍历左子树，然后遍历右子树，最后访问树的根节点。
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


# print(TreeNode.generate([1, 2, 3, None, None, 4, 5]))


class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
