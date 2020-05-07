#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Create at 2020/5/6

from typing import *


class Solution:
    def queryString(self, S: str, N: int) -> bool:
        if N < 2:
            return bin(N)[2:] in S
        for i in range(N >> 1, N + 1):
            a: str = bin(i)[2:]
            if a not in S:
                return False
        return True


so = Solution()
print(so.queryString("0110", 3))
print(so.queryString("0110", 4))
