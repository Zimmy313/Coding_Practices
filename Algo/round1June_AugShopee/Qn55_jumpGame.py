from typing import *

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maximum = -1
        n = len(nums)
        
        if n == 1:
            return True
        
        for i in range(n):
            maximum = max(maximum, i+nums[i]) # furthese index reachable currently
            
            if maximum >= n-1: # terminate early if we can be sure that we can reach
                return True
            
            if i >= maximum: # stop if you are stuck. Maximumly stuck at i
                return False
        return True
            

if __name__ == "__main__":
    solver = Solution()
    nums = [3,2,1,0,4]
    print(solver.canJump(nums))