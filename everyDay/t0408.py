#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Create at 2020/4/8

from typing import *

"""https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/"""


class Solution:
    """ BFS or DFS"""
    def movingCount(self, m: int, n: int, k: int) -> int:
        def calcSi(i, si):
            return si + 1 if (i + 1) % 10 else si - 8

        def dfs(i, j, si, sj):
            if not 0 <= i < m or not 0 <= j < n or k < si + sj or (i, j) in visited:
                return 0
            visited.add((i, j))
            return 1 + dfs(i + 1, j, calcSi(i, si), sj) + dfs(i, j + 1, si, calcSi(j, sj))

        visited = set()
        return dfs(0, 0, 0, 0)
