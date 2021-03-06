#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Create at 2020/4/28
import functools
from typing import *


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        ret = functools.reduce(lambda x, y: x ^ y, nums)
        div = 1
        while div & ret == 0:
            div <<= 1
        a, b = 0, 0
        for n in nums:
            if n & div:
                a ^= n
            else:
                b ^= n
        return [a, b]


nums = [4, 6, 4, 2]
so = Solution()
so.singleNumbers(nums)
