from typing import *

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_row = len(matrix)
        n_col = len(matrix[0])
        left, right = 0, n_row*n_col - 1
        
        while left <= right:
            
            mid = left + (right - left)//2
            row = mid // n_col 
            col = mid % n_col 
            
            current = matrix[row][col]
            
            if current == target: 
                return True
            
            elif current < target: 
                left = mid + 1
            
            else:
                right = mid - 1
        return False 
    
if __name__ == "__main__":
    s = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    print(s.searchMatrix(matrix, target))