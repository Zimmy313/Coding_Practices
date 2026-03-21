from typing import *

class Solution:
    def jump(self, nums: List[int]) -> int:
        result = 0
        pos = 0 
        
        while pos < len(nums) - 1:
            best = 0
            end = pos + nums[pos] + 1
            result += 1
            
            if end >= len(nums): # terminate early
                return result 
            
            for i in range(pos, end): # finding the longest step
                if nums[i] + i > best:
                    best = nums[i] + i
                    next_pos = i  # updating position
            pos = next_pos
            
        return result
            
            
            
if __name__ == "__main__":
    s = Solution()
    nums = [1,1,1,1]
    print(s.jump(nums))