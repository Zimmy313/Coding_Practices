from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        
        while left != right:
            current = numbers[left] + numbers[right]
            
            if current == target:
                return [left+1, right+1]
            elif current > target:
                right -= 1 
            else:
                left += 1
            


if __name__ == "__main__":
    numbers = list(map(int,input("Please input numbers:").split(",")))
    target = int(input("Please input target:"))
    solver = Solution()
    
    print(solver.twoSum(numbers, target))
    
            