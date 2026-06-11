from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set()
        result = 0
        
        for i in range(len(nums)):
            lookup.add(nums[i])
        
        for num in nums:
            counter = 1
            
            if (num-1) not in lookup:
                next = num + 1
                
                while next in lookup:
                    counter += 1
                    next += 1
                
            if counter > result:
                result = counter
        
        return result 
    
if __name__ == "__main__":
    nums = list(map(int, input("Please input nums:\n").split(",")))
    solver = Solution()
    
    print(solver.longestConsecutive(nums))
