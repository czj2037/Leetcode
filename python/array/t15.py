#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Create By c00417123 at 2020/4/2
from typing import *


class Solution:
    """去重和双指针,[-2,0,0,2,2],[-1, 0, 1, 2, -1, -4]"""

    def __twoSum(self, nums: List[int], target: int, x: int) -> List[List[int]]:
        res = []
        i, j = x, self.n - 1
        while i < j:
            if i > x and nums[i] == nums[i - 1]:
                i += 1
                continue
            if nums[i] + nums[j] == target:
                res.append([nums[j], nums[i]])
                i += 1
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                j -= 1
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.n = len(nums)
        res = []
        x = 0
        while x < self.n - 2:
            if x > 0 and nums[x] == nums[x - 1]:
                x += 1
                continue
            two_res = self.__twoSum__(nums, -nums[x], x + 1)
            for t in two_res:
                t.append(nums[x])
                t.reverse()
                res.append(t)
            x += 1
        return res

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        """超出时间限制"""
        nums.sort()
        self.n = len(nums)
        res = set()
        x = 0
        while x < self.n - 2:
            two_res = self.__twoSum(nums, -nums[x], x + 1)
            for t in two_res:
                t.append(nums[x])
                t.reverse()
                res.add(tuple(t))
            x += 1
        res2 = [list(r) for r in res]
        return res2


so = Solution()
print(so.threeSum([-1, 0, 1, 2, -1, -4]))
