#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# create by czj at 2020/4/7
from typing import List


class Solution:
    """
    实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
[1,3,2]->[2,1,3]
[4,2,0,2,3,2,0]->[4,2,0,3,0,2,2]"


"""

    def nextPermutation(self, nums: List[int]) -> None:
        """贪心算法 从最后一个开始算"""
        if nums is None or len(nums) == 0:
            return
        n = len(nums)
        i = n - 2
        while i > -1:
            j = n - 1
            while j > i:
                if nums[j] > nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    b = nums[i + 1:]
                    b.sort()
                    nums[i + 1:] = b
                    return
                j -= 1
            i -= 1
        nums.sort()


def printList(nums: List[int]) -> None:
    Solution().nextPermutation(nums)
    print(nums)


nums1 = [1, 2, 3]
nums2 = [3, 2, 1]
nums3 = [1, 1, 5]
printList(nums1)
printList(nums2)
printList(nums3)
printList([1, 3, 2])
printList([4, 2, 0, 2, 3, 2, 0])
