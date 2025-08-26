from typing import *

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        table = set(nums)
        result = 0
        for num in table:
            number = num
            count = 0
            
            if number - 1 not in table: # start of new sequence
                count += 1
                while number + 1 in table:
                    count += 1
                    number += 1
                result = max(count, result)
            else:
                continue
        return result 
    
                


if __name__ == "__main__":
    s= Solution()
    nums = [0,3,7,2,5,8,4,6,0,1]
    print(s.longestConsecutive(nums))
    