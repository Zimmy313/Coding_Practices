from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i, num in enumerate(nums):
            need = target - num
            
            if need in seen:
                return([seen[need], i])
            
            seen[num] = i
                   
        return [] 
    
    

if __name__ == "__main__":
    nums = list(map(int, input("Please input nums:\n").split()))
    target = int(input("Please input target:\n"))
    
    solver = Solution()
    
    print(solver.twoSum(nums, target))    