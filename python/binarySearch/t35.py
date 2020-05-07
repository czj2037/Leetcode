#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Create at 2020/5/7

from typing import *


class Solution:
    # 因为mid是靠向左侧，所以当剩下两个数时，必然是 l，target，r这样的顺序
    # 再次迭代：target l=r,必然会变成 r,target,l，此时target刚好插入到l所在位置
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (r - l) // 2 + l
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return l


so = Solution()
print(so.searchInsert([1, 3, 5, 6], 5))
print(so.searchInsert([1, 3, 5, 6], 2))
print(so.searchInsert([1, 3, 5, 6], 7))
print(so.searchInsert([1, 3, 5, 6], 0))
print(so.searchInsert([1], 1))
