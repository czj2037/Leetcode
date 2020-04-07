#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Create at 2020/4/7

from typing import *


class Solution:
    """
    https://leetcode-cn.com/problems/rotate-matrix-lcci/submissions/
    给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。
    不占用额外内存空间能否做到？
    给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],
原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
    Do not return anything, modify matrix in-place instead.
    """

    def __rotate(self, matrix: List[List[int]], x, m) -> None:
        """(x,y)左上角的点, (m,n)用下角的点 """
        y = x
        n = m
        if m <= x:
            return
        for i in range(n - y):
            t = matrix[x][y + i]
            matrix[x][y + i] = matrix[m - i][y]
            matrix[m - i][y] = matrix[m][n - i]
            matrix[m][n - i] = matrix[x + i][n]
            matrix[x + i][n] = t
        self.__rotate(matrix, x + 1, m - 1)

    def rotate(self, matrix: List[List[int]]) -> None:
        self.__rotate(matrix, 0, len(matrix) - 1)


# matrix1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# 
# matrix2 = [
#     [5, 1, 9, 11],
#     [2, 4, 8, 10],
#     [13, 3, 6, 7],
#     [15, 14, 12, 16]
# ]
# 
# so = Solution()
# so.rotate(matrix1)
# so.rotate(matrix2)
# print(matrix1)
# print(matrix2)
