#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Create at 2020/4/28

from typing import *


class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        return max(len(a), len(b))

    def __isSub(self, s1: str, s2: str):
        i = 0
        n1 = len(s1)
        for s in s2:
            if i < n1 and s1[i] == s:
                i += 1
        return i == n1

    def findLUSlength_521(self, strs: List[str]) -> int:
        m = -1
        for i, s in enumerate(strs):
            flag = True
            for j, t in enumerate(strs):
                if i == j:
                    continue
                elif self.__isSub(s, t):
                    flag = False
                    break
            if flag:
                m = max(m, len(s))
        return m


so = Solution()
# print(so.findLUSlength('abc', 'bbcd'))
print(so.findLUSlength_521(["aba", "cdc", "eae"]))
print(so.findLUSlength_521(["aaa", "aaa", "aa"]))
print(so.findLUSlength_521(["aabbcc", "aabbcc", "cb", "abc"]))
