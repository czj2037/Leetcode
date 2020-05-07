#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Create at 2020/5/7

from typing import *


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ma = 0
        for i in range(n):
            a = set()
            for j in range(i, n):
                if s[j] in a:
                    break
                else:
                    a.add(s[j])
            ma = max(len(a), ma)
        return ma


so = Solution()
print(so.lengthOfLongestSubstring('abcabcbb'))
print(so.lengthOfLongestSubstring('bbbbb'))
print(so.lengthOfLongestSubstring('pwwkew'))
