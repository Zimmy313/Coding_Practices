from typing import *
from collections import defaultdict, Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int: # using Boyer-Moore Majority Voting Algorithm
        count = 0
        candidate = None
        
        for num in nums:
            
            if count == 0:
                candidate = num 
            

            if candidate == num:
                count += 1
            else:
                count -= 1
                
        return candidate
    
    def majorityElement2(self, nums: List[int]) -> int: # using Counter
        ctr = Counter(nums)
        return max(ctr, key = ctr.get)
        
    def majorityElement1(self, nums: List[int]) -> int:
        table = defaultdict(int)
        
        for num in nums:
            table[num] += 1
            
        result = None
        maximum = 0
        for key, value in table.items():
            if value > maximum:
                maximum = value 
                result = key 
                
        return result
        