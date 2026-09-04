class Solution:
    def rob(self, nums: List[int]) -> int:
        seen = {}
        
        def helper(n : int):
            
            if n == 0:
                seen[0] = nums[0]
                return nums[0]
            elif n == 1:
                seen[1] = max(nums[0], nums[1])
                return seen[1]

            elif n in seen:
                return seen[n]
            
            else:
                result = max(helper(n-2) + nums[n], helper(n-1)) 
                seen[n] = result
                return result

        return helper(len(nums)-1)