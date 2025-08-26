from typing import *
from collections import deque 

class Solution:    
    def productExceptSelf1(self, nums: List[int]) -> List[int]: # can be shortened to 2 passes: process result 
                                                                # twice while building pre and sub 
        pre = []
        sub = deque()
        result = []
        
        accumulation = 1
        for num in nums:
            accumulation *= num
            pre.append(accumulation)
        
        
        accumulation = 1
        for i in range(len(nums)-1, -1, -1):
            accumulation *= nums[i]
            sub.appendleft(accumulation)
        result.append(sub[1])
        
        for i in range(1, len(nums)- 1):
            product = pre[i-1] * sub[i+1]
            result.append(product)
        result.append(pre[len(nums)-2])
        
        return result

if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3,4]
    print(s.productExceptSelf(nums = nums))