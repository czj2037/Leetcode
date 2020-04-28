#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Create at 2020/4/28

from typing import *


class Solution:
    """
    方法三：动态规划
    方法四：中心扩展算法
    """

    # 动态规划 参考答案:
    def longestPalindrome2(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        dp = [[False for _ in range(n)] for _ in range(n)]
        lon = 1
        st = 0
        for i in range(n):
            dp[i][i] = True
        for j in range(1, n):
            for i in range(0, j):
                if s[i] == s[j]:
                    # dp[i + 1][j - 1] 就得考虑边界情况=>  i+1 >=j-1
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                    if dp[i][j] and j + 1 - i > lon:
                        st, lon = i, j + 1 - i
                else:
                    dp[i][j] = False

        return s[st:st + lon]

    # 动态规划  # [i,j)
    def longestPalindrome3(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ''
        res = []
        for i in range(n):
            res.append([0] * (n + 1))
            res[i][i] = 1
            res[i][i + 1] = 1
        res[n - 1][n] = 1
        a, b = 0, 1
        for d in [x + 1 for x in range(n - 1)]:
            for i in range(n - d):
                if s[i] == s[i + d] and res[i + 1][i + d] == 1:
                    res[i][i + d + 1] = 1
                    if d + 1 > b - a:
                        a, b = i, i + d + 1
                else:
                    res[i][i + d + 1] = 0
        return s[a:b]

    # 中心扩散法
    def longestPalindrome4(self, s: str) -> str:
        if not s:
            return ''
        n = len(s)
        a, b = 0, 1
        for i in range(n):
            l, r = i - 1, i + 1
            while l > -1 and r < n and s[l] == s[r]:
                if r + 1 - l > b - a:
                    a, b = l, r + 1
                l -= 1
                r += 1
            l, r = i, i + 1
            while l > -1 and r < n and s[l] == s[r]:
                if r + 1 - l > b - a:
                    a, b = l, r + 1
                l -= 1
                r += 1
        return s[a:b]


so = Solution()
# print(so.longestPalindrome3('abcba'))
# print(so.longestPalindrome3('abba'))
# print(so.longestPalindrome3('cbbd'))
# print(so.longestPalindrome3('bab'))


# print(so.longestPalindrome4(''))
# print(so.longestPalindrome4('abcba'))
# print(so.longestPalindrome4('abba'))
# print(so.longestPalindrome4('cbbd'))
# print(so.longestPalindrome4('bab'))

print(so.longestPalindrome2(''))
print(so.longestPalindrome2('abcba'))
print(so.longestPalindrome2('abba'))
print(so.longestPalindrome2('cbbd'))
print(so.longestPalindrome2('bab'))
