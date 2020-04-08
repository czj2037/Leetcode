#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Create at 2020/4/8
from bisect import bisect_left
from typing import *

"""假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
你可以假设数组中不存在重复的元素。
你的算法时间复杂度必须是 O(log n) 级别。

示例 1:
输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4

示例 2:
输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1"""


class Solution:
    def __rotateIndex(self, nums: List[int], m: int, n: int):
        if n - m == 1:
            return m
        k: int = (n - m) // 2 + m
        a, b, c = nums[m], nums[k], nums[n - 1]
        if c <= a <= b:
            return self.__rotateIndex(nums, k, n)
        elif b <= c <= a:
            return self.__rotateIndex(nums, m, k)
        else:
            return n - 1

    def __binary_serarch(self, nums: List[int], m: int, n: int, target: int) -> int:
        if m >= n:
            return -1
        k = (n - m) // 2 + m
        a, b, c = nums[m], nums[k], nums[n - 1]
        if b == target:
            return k
        elif target < b:
            return self.__binary_serarch(nums, m, k, target)
        else:
            return self.__binary_serarch(nums, k + 1, n, target)

    def search(self, nums: List[int], target: int) -> int:
        if nums is None or len(nums) == 0:
            return -1
        n = len(nums)
        h = self.__rotateIndex(nums, 0, n)
        if target < nums[0]:
            return self.__binary_serarch(nums, h + 1, n, target)
        else:
            return self.__binary_serarch(nums, 0, h + 1, target)


def soAndPrint(nums: List[int], target: int) -> None:
    so = Solution()
    print(so.search(nums, target))


soAndPrint([4, 5, 6, 7, 0, 1, 2], 0)
soAndPrint([4, 5, 6, 7, 0, 1, 2], 3)
