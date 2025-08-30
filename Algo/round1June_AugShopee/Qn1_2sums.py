from typing import *

class Solution:
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        
        # bruteforcely start at all position and try other combination ==> O(n^2)
        
        for i in range(len(nums)):
            current = nums[i]
            for j in range(i+1,len(nums)):
                current2 = nums[j]
                
                if current + current2 == target:
                    return [i,j]
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        # faster 
        for i in range(len(nums)):
            result = target - nums[i]
            
            if result not in table:
                table[nums[i]] = i
            else:
                d = table[result]
                return [d,i]
            
                


if __name__ == "__main__":
    s = Solution()
    nums = [2,7,11,15]
    target = 9
    
    print(s.twoSum(nums, target))