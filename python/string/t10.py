#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Create at 2020/4/30

from typing import *

import re
from array import array
array('l', [1, 2, 3, 4, 5])

class Solution:
    # 动态规划
    def isMatch2(self, s: str, p: str) -> bool:
        dp = {}
        if not p:
            return not s
        # dp[(0, 0)] = bool(s) and p[0] in {s[0], '.'}

        m, n = len(s), len(p)
        dp[(-1, -1)] = True
        for x in range(n):
            dp[(-1, x)] = (p[x] == '*') and (dp[(-1, x - 2)])
        for x in range(m):
            dp[(x, -1)] = False
        for i in range(m):
            for j in range(n):
                if p[j] != '*':
                    dp[(i, j)] = p[j] in {s[i], '.'} and dp[(i - 1, j - 1)]
                else:
                    if p[j - 1] in {s[i], '.'}:
                        dp[(i, j)] = dp[(i, j - 2)] or dp[(i, j - 1)] or dp[(i - 1, j)]
                    else:
                        dp[(i, j)] = dp[(i, j - 2)]

        return dp[(m - 1, n - 1)]

    # 回溯法
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        first_match = bool(s) and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*':
            # 匹配0个； 匹配1个或者多个
            return self.isMatch(s, p[2:]) or first_match and self.isMatch(s[1:], p)
        else:
            return first_match and self.isMatch(s[1:], p[1:])


so = Solution()
# print(so.isMatch('aa', 'a'))
# print(so.isMatch('aa', 'a*'))
# print(so.isMatch('aa', '.*'))
print(so.isMatch2("aab", "c*a*b"))
