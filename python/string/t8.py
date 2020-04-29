#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Create at 2020/4/29

from typing import *
import string
import functools


# https://leetcode-cn.com/problems/string-to-integer-atoi/solution/zi-fu-chuan-zhuan-huan-zheng-shu-atoi-by-leetcode-/  题解
class Auto(object):
    def __init__(self):
        self.state = 'start'
        self.ans = 0
        self.sign = 1
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }

    def __getCol(self, c: str):
        if c.isspace():
            return 0
        elif c in ['+', '-']:
            return 1
        elif c.isdigit():
            return 2
        return 3

    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1


class Solution1:
    def myAtoi(self, st: str) -> int:
        s = st.strip()
        ss = ['-', '+'] + list(map(lambda a: str(a), range(10)))
        if (not s) or (s[0:1] not in ss) or (len(s) == 1 and s[0:1] in ['-', '+']):
            return 0
        i = 0
        for v in s:
            i += 1
            if v not in ss:
                i -= 1
                break
        a = min(2 ** 31 - 1, int(s[0:i]))
        a = max(-2 ** 31, a)
        return a


INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31


class Automaton:
    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }

    def get_col(self, c):
        if c.isspace():
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1


class Solution2:
    def myAtoi(self, str: str) -> int:
        automaton = Automaton()
        for c in str:
            automaton.get(c)
        return automaton.sign * automaton.ans


so = Solution2()
print(so.myAtoi("42"))
print(so.myAtoi("   -42"))
print(so.myAtoi("4193 with words"))
print(so.myAtoi('3.1415'))
print(so.myAtoi('+'))
