class Solution:
    def robLinear(self, nums: List[int]) -> int:
        robbed = {}

        def helper(n):
            if n in robbed:
                return robbed[n]
            if n == 0:
                robbed[0] = nums[0]
                return nums[0]
            if n == 1:
                robbed[1] = max(nums[0], nums[1])
                return robbed[1]

            robbed[n] = max(helper(n-1), helper(n-2) + nums[n])
            return robbed[n]
        
        return helper(len(nums)-1)


    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        result1 = self.robLinear(nums[0:n-1])
        result2 = self.robLinear(nums[1:n])

        return max(result1, result2)

        