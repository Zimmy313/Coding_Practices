from typing import List 
import sys

class Solution:
    def productExceptSelf(self, nums:List[int])-> List[int]:
        pre, sub = [], []
        result = []
        temp1, temp2 = 1,1
        for i in range(len(nums)):
            if i == 0:
                temp1, temp2 = temp1, temp2
            else:
                temp1 = temp1 * nums[i-1]
                temp2 = temp2 * nums[-i]
                
            pre.append(temp1)
            sub.append(temp2)
        for i in range(len(nums)):
            result.append(pre[i] * sub[-i-1])
            
        return result 
    

if __name__ == "__main__":
    solver = Solution()
    nums = list(map(int, input().split(",")))
    
    print(solver.productExceptSelf(nums))
    