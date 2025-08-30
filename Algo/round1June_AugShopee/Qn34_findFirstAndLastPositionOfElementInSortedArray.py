from typing import *

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left, right = 0, len(nums)-1
        start = None
        end = None
        while left <= right:
            mid = (right + left) // 2
            
            if nums[mid] == target:
                if mid != 0: # avoiding index out of range
                    pre = nums[mid-1]
                    
                    if pre == target: # start not found
                        right = mid -1 
                    elif pre < target:
                        start = mid 
                        break
 
                else:
                    start = 0
                    break
                
            
            elif nums[mid] < target:
                left = mid + 1
                
            else:
                right = mid - 1
            
        if start is None:
            return [-1,-1]
        
        # left BS
        left, right = start+1, len(nums) - 1
        
        while left <= right:
            mid = (right + left) //2 
            
            if nums[mid] == target:
                if mid != (len(nums)-1): # avoiding index out of range
                    next = nums[mid+1]
                    
                    if next == target: # end not found
                        left = mid + 1 
                    elif next > target:
                        end = mid 
                        break 
 
                else:
                    end = len(nums) -1
                    break
                
            
            elif nums[mid] < target:
                left = mid + 1
                
            else:
                right = mid - 1
        
        if end is None:
            return [start,start]
        return [start, end]
            
            
         
            