from typing import *

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        dif = numbers[left] + numbers[right]
        
        while dif != target:
            
            if dif > target:
                right -= 1
                dif = numbers[left] + numbers[right]
                
            else:
                left += 1
                dif = numbers[left] + numbers[right]
                
        return [left+1, right+1]

if __name__ == "__main__":
    s = Solution()
    test = [2,7,11,15]
    print(s.twoSum(test, 9))