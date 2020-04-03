#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Create By c00417123 at 2020/4/3
import sys
from typing import List


class Solution:
    """给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
        例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
        与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2)."""

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[0:3])
        n = len(nums)
        x = 0
        while x < n:
            # 当数据是负数的时候，失效
            # if nums[x] > target:
            #     break
            if x > 0 and nums[x] == nums[x - 1]:
                continue
            i = x + 1
            j = n - 1
            while i < j:
                t_sum = nums[x] + nums[i] + nums[j]
                if abs(target - res) > abs(target - t_sum):
                    res = t_sum
                if target == t_sum:
                    return t_sum
                elif target - t_sum > 0:
                    i += 1
                else:
                    j -= 1
            x += 1
        return res

    def threeSumClosest_2(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        res = float("inf")
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            L = i + 1
            R = n - 1
            while L < R:
                cur_sum = nums[i] + nums[L] + nums[R]
                if cur_sum == target:
                    return target
                if abs(cur_sum - target) < abs(res - target):
                    res = cur_sum
                if cur_sum - target < 0:
                    L += 1
                else:
                    R -= 1
        return res


print(Solution().threeSumClosest([-1, 2, 1, -4], 1))
print(Solution().threeSumClosest(
    [6, -18, -20, -7, -15, 9, 18, 10, 1, -20, -17, -19, -3, -5, -19, 10, 6, -11, 1, -17, -15, 6, 17, -18, -3, 16, 19,
     -20, -3, -17, -15, -3, 12, 1, -9, 4, 1, 12, -2, 14, 4, -4, 19, -20, 6, 0, -19, 18, 14, 1, -15, -5, 14, 12, -4, 0,
     -10, 6, 6, -6, 20, -8, -6, 5, 0, 3, 10, 7, -2, 17, 20, 12, 19, -13, -1, 10, -1, 14, 0, 7, -3, 10, 14, 14, 11, 0,
     -4, -15, -8, 3, 2, -5, 9, 10, 16, -4, -3, -9, -8, -14, 10, 6, 2, -12, -7, -16, -6, 10], -52))
