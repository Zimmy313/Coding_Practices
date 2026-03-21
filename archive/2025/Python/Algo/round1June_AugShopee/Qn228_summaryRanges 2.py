from typing import *

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        start = None
        
        if not nums:
            return []
        
        for i in range(len(nums)+1):
            if start is None:
                start = nums[i]
                pre = nums[i]
                
            elif i == len(nums) : # reaching the end. has to stop
                if start != pre:
                    range1 = str(start) + "->" + str(pre)
                    result.append(range1)
                else:
                    range1 = str(start)
                    result.append(range1)
            
            elif nums[i] - pre == 1: # building the range
                pre = nums[i]
            
            else:
                
                if start != pre:
                    range1 = str(start) + "->" + str(pre)
                    result.append(range1)
                    start = nums[i]
                    pre = nums[i]
                else:
                    range1 = str(start)
                    result.append(range1)
                    start = nums[i]
                    pre = nums[i]
        return result