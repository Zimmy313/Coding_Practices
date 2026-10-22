class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -float("inf")

        left = 1
        right = 1

        for i in range(len(nums)):
            left = left * nums[i]
            right = right * nums[-i - 1]

            res = max(res, left, right)

            if left == 0:
                left = 1
            
            if right == 0:
                right = 1
        
        return res