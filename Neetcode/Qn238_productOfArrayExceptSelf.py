class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        post = [1] * len(nums)
        result = []

        for i in range(1, len(nums)):
            pre[i] = nums[i-1] * pre[i-1]
        
        for i in range(len(nums) - 2, -1, -1):
            post[i] = post[i+1] * nums[i+1]

        for i in range(len(nums)):
            result.append(pre[i] * post[i])

        
        return result

        