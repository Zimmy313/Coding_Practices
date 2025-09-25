from typing import *

class Solution:
    def removeElement1(self, nums: List[int], val: int) -> int:
        k = 0
        temp = []
        for num in nums:
            if num != val:
                k += 1
                temp.append(num)
        
        for i in range(k):
            nums[i] = temp[i]
        
        return k
    
    def removeElement(self, nums: List[int], val: int) -> int:
        
        counts = nums.count(val)
        for i in range(counts):
            nums.remove(val)
        return len(nums)
    
            
    
if __name__ == "__main__":
    solver = Solution()
    
    print(solver)
        