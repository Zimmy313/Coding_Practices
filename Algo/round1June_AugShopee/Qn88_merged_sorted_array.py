from typing import *
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        p = n + m -1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] <= nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1

            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1


    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None: # faster
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m + n -1] = nums1[m-1]
                m -= 1
            else:
                nums1[m + n -1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]

