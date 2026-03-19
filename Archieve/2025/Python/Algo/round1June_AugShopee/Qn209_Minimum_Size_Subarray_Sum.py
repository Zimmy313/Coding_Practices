from typing import *

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        min_len = float("inf")
        cur_sum = 0
        cur_length = 0
        
        while right < len(nums):
            cur_sum += nums[right]
            cur_length += 1
            right += 1
            
            while cur_sum >= target and left < len(nums):
                
                if min_len >= cur_length:
                    min_len = cur_length
                
                cur_sum -= nums[left]
                cur_length -= 1
                left += 1
        if min_len == float("inf"):
            return 0
        return min_len
                
                
                
            

if __name__ == "__main__":
    s = Solution()
    test = [2,3,1,2,4,3]
    print(s.minSubArrayLen(7,test))
                
                
              #[1,1,1,1,1,1,1,1]   
#  