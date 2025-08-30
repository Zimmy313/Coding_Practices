from typing import *

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        left =  0

        for right in range(1,len(nums)):
            current = nums[right]
            
            if current == nums[left]:
                continue
            
            else:
                left += 1
                nums[left] = current
 
        return left + 1

if __name__ == "__main__":
    s = Solution()
    nums = [1,1,2]
    
    print(s.removeDuplicates(nums))
        
        