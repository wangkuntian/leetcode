#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project__ =  'leetcode'
__file__    =  '__init__.py.py'
__author__  =  'king'
__time__    =  '2020/2/22 20:40'


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
难度：简单

设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x)-- 将元素 x 推入栈中。
pop()-- 删除栈顶的元素。
top()-- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。
示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
"""


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.main = []
        self.min = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.main.append(x)
        if not self.min or x <= self.min[-1]:
            self.min.append(x)

    def pop(self):
        """
        :rtype: None
        """
        item = self.main.pop()
        if item == self.min[-1]:
            self.min.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.main[-1] if self.main else None

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1] if self.min else None


obj = MinStack()
obj.push(1)
a = obj.top()
b = obj.getMin()
obj.pop()
print(a)
print(b)
