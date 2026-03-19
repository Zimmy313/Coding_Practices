from typing import *

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minimum = float("inf")
        left  = 0 
        cur_sum = 0
        for right in range(len(nums)):
            cur_sum += nums[right]
            
            while cur_sum >= target and left <= len(nums) - 1:
                cur_sum -= nums[left]
                minimum = min(minimum, right - left + 1)
                left += 1
                
        return minimum if minimum != float("inf") else 0
                        
        
        
    def minSubArrayLen1(self, target: int, nums: List[int]) -> int:# TLE
        minimum = float("inf")
        flag = False # to test if target has ever been reached
        
        if nums[-1] >= target or nums[0] >= target:
            return 1
        
        for left in range(len(nums)-1):
            right = left + 1
            cur_sum = nums[left] + nums[right]
        
            while cur_sum < target and right <= len(nums) - 2:
                right += 1
                cur_sum += nums[right]
                
            if cur_sum >= target and right - left < minimum:
                minimum = right - left + 1
                flag = True
        if not flag:
            return 0
        else:
            return minimum
            
            
        
        


if __name__ == "__main__":
    solver = Solution()
    target = 7
    nums = [2,3,1,2,4,3]
    
    print(solver.minSubArrayLen(target, nums))