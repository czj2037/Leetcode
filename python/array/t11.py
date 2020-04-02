#!/usr/bin/python3
# -*- coding: utf-8 -*-

#11. 盛最多水的容器
# Create By c00417123 at 2020/4/1
from typing import List


class Solution:
    '双指针法'

    def maxArea(self, height: List[int]) -> int:
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            temp = min(height[i], height[j]) * (j - i)
            if res < temp:
                res = temp
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return res


so = Solution()
print(so.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
