from typing import *
from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool: # keep last seen index
        
        table = {}
        
        for i in range(len(nums)):
            
            current = nums[i]
            
            if current in table:
                index  = table[current]
                
                if abs(index - i) <= k:
                    return True 
            
            table[current] = i 
        return False
        
        
    
    def containsNearbyDuplicate1(self, nums: List[int], k: int) -> bool: # not optimal
        table = defaultdict(list)
        
        for i in range(len(nums)):
            table[nums[i]].append(i)
            
        for key, value in table.items():
            
            if len(value) == 1:
                continue
            
            for i in range(len(value)):
                for j in range(i+1, len(value)):
                    dif = abs(value[j] - value[i])
                    if dif <= k:
                        return True
                    
        return False

if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3,1,2,3]
    k = 2
    print(s.containsNearbyDuplicate(nums,k))
        