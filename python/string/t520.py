#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Create at 2020/4/28

from typing import *


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
        if n < 2:
            return True
        if word[0:1].islower():
            return word[1:].islower()
        else:
            return word[1:].islower() or word[1:].isupper()
