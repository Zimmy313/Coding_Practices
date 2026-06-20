from typing import List

class Solution:
                
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        results = []
        
        for i in range(n-2):
            
            left = i+1
            right = n-1
            target = -nums[i]
            
            if i != 0:
                if nums[i] == nums[i-1]:
                    continue
            
            while left < right:
                current = nums[left] + nums[right]
                
                if current == target:
                    result = [-target, nums[left], nums[right]]
                    
                    if len(results) == 0:
                        results.append(result)
                    else:
                        pre = results.pop()
                        if pre != result:
                            results.append(pre)
                        results.append(result)
                
                    left += 1
                    right -= 1
                
                elif current > target:
                    right -= 1
                else:
                    left += 1
                
        return results
    
if __name__ == "__main__":
    nums = list(map(int, input("Please input nums:").split(",")))
    
    solver = Solution()
    print(solver.threeSum(nums=nums))