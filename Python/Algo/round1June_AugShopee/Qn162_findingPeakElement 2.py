from typing import *

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) -1

        while left < right: # continues only when there are at least 2 elements left

            mid = (right + left) // 2

            if nums[mid] < nums[mid + 1]:
                left = mid + 1

            else:
                right = mid 
        return left
            