from typing import *

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (right + left) //2 
    
            if nums[mid] == target:
                return mid
    
            if nums[mid] < nums[right]: # right side is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
    
            else: # left side is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1 
        
        
# there is another solution of using 2 passes binary search. First find the 'k'. Feels tricky how to do that.

    def search_twoPasses(self, nums: List[int], target: int) -> int:
            n = len(nums)

            # Step 1: Find rotation index
            # using the idea of smallest. smallest must be at the start of the orininal array. Finding it gives us the 'k'
            left, right = 0, n - 1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > nums[right]: # smallest is on the right
                    left = mid + 1
                else:
                    right = mid
            k = left  # smallest element index

            # Step 2: Adjusted binary search
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                real_mid = (mid + k) % n
                if nums[real_mid] == target:
                    return real_mid
                elif nums[real_mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return -1