from typing import *

class Solution:
    def threeSum1(self, nums: List[int]) -> List[List[int]]: # TLE
        
        table1 = {}
        
        for i in range(len(nums)): # building a dictionary for quick reference
            
            if nums[i] not in table1:
                table1[nums[i]] = [i]
            else:
                table1[nums[i]].append(i)
        
        result = []
        
        for left in range(len(nums)):
            
            for right in range(left+1, len(nums)):
                
                remaining = -nums[left] - nums[right]
                
                if remaining in table1:
                    
                    for index in table1[remaining]:
                        if index > right:
                            temp1 = [nums[left], nums[right], nums[index]]
                            temp1.sort()
                            if temp1 not in result:
                                result.append(temp1)
        return result 
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        results=[]

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            goal = nums[i]
            
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    results.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # need to handle duplicate as for the same number, there is exactly one way to sum up to another number
                    
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                        
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
                
                elif total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
            
        return results
    
                
                
            
            
            
    
if __name__ == "__main__":
    s = Solution()
    nums = [-1,0,1,2,-1,-4]
    print(s.threeSum(nums))