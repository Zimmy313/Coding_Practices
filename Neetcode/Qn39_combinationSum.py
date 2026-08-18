class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(start, total):
            if total == target:
                res.append(path.copy())
                return 
            
            if total > target:
                return 
            
            for i in range(start, len(nums)):
                path.append(nums[i])

                dfs(i, total + nums[i])

                path.pop()

        dfs(0,0)
    
        return res
            


        
            