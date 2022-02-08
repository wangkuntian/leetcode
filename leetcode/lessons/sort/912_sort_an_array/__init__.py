#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project__ =  'leetcode'
__file__    =  '__init__.py'
__author__  =  'king'
__time__    =  '2020/2/21 01:34'


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
难度：中等

给定一个整数数组nums，将该数组升序排列。

示例 1：
输入：[5,2,3,1]
输出：[1,2,3,5]

示例 2：
输入：[5,1,1,2,0,0]
输出：[0,0,1,1,2,5]

提示：
1 <= A.length <= 10000
-50000 <= A[i] <= 50000
"""


class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return sorted(nums)

    def quick_sort(self, nums, l, r):
        if l >= r:
            return
        left = l
        right = r
        pivot = nums[l]

        while left < right:
            while left < right and nums[right] >= pivot:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] <= pivot:
                left += 1
            nums[right] = nums[left]

        nums[left] = pivot
        self.quick_sort(nums, l, right - 1)
        self.quick_sort(nums, left + 1, r)

    def bubble_sort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(0, len(nums) - 1):
            for j in range(0, len(nums) - 1 - i):
                # print(i)
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums

    def selection_sort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        for i in range(length):
            for j in range(i, length):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums

    def insertion_sort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1, len(nums)):
            while i and nums[i] < nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
                i -= 1
        return nums

    def shell_sort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        gap = length // 2
        while gap:
            for i in range(gap, length):
                while i - gap >= 0 and nums[i - gap] > nums[i]:
                    nums[i - gap], nums[i] = nums[i], nums[i - gap]
                    i -= gap
            gap //= 2
        return nums

    def merge_sort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result

    def merge_sort2(self, nums, l, r):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if l == r:
            return
        mid = (l + r) // 2
        self.merge_sort2(nums, l, mid)
        self.merge_sort2(nums, mid + 1, r)
        temp = []
        i = l
        j = mid + 1
        while i <= mid or j <= r:
            if i > mid or (j <= r and nums[j] < nums[i]):
                temp.append(nums[j])
                j += 1
            else:
                temp.append(nums[i])
                i += 1
        nums[l:r + 1] = temp

    def heapify(self, nums, start, end):
        item = nums[start]
        index = start
        l = index * 2 + 1
        r = index * 2 + 2
        while l < end:
            if r < end and nums[r] >= nums[p]:
                p = r
            if item < nums[p]:
                nums[p] = nums[p]

    def heap_sort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """


nums = [5, 4, 3, 2, 1]
print(Solution().sortArray(nums))
nums = [5, 4, 3, 2, 1]
Solution().quick_sort(nums, 0, len(nums) - 1)
print(nums)

# nums = [5, 4, 3, 2, 1]
print(Solution().bubble_sort(nums))
nums = [5, 4, 3, 2, 1]
print(Solution().selection_sort(nums))
# nums = [5, 4, 3, 2, 1]
print(Solution().insertion_sort(nums))

nums = [5, 4, 3, 2, 1]
print(Solution().shell_sort(nums))

nums = [5, 4, 3, 2, 1]
print(Solution().merge_sort(nums))

nums = [5, 4, 3, 2, 1]
Solution().merge_sort2(nums, 0, len(nums) - 1)
print(nums)
