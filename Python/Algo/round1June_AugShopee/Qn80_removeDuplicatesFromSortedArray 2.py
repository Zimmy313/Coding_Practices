from typing import *

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left  = 0
        table = []
        
        for right in range(len(nums)):
            current_num = nums[right]
            
            if current_num not in table:
                nums[left] = current_num
                left += 1
                table = [current_num]
            
            elif current_num in table and len(table) < 2:
                nums[left] = current_num 
                left += 1
                table.append(current_num)
            else:
                table.append(current_num)
                
        return left

if __name__ == "__main__":
    s = Solution()
    nums = [1,1,1,2,2,3]
    print(s.removeDuplicates(nums))