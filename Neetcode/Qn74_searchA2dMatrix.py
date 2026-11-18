from typing import List
import ast

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        l, r = 0, m

        while l < r:
            mid = (r - l) // 2 + l

            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                if matrix[mid][n-1] >= target:
                    break
                l = mid + 1
            else:
                r = mid

        selected = matrix[mid]
        
        l, r = 0, n
        
        while l < r:
            mid = (r - l) // 2 + l
            
            if selected[mid] == target:
                return True
            elif selected[mid] < target:
                l = mid + 1
            else:
                r = mid
        
        return False
    

if __name__ == "__main__":
    solver = Solution()
    
    matrix = ast.literal_eval(input("Please input matrix:"))
    target = int(input("Please input the target value:"))
    
    print(solver.searchMatrix(matrix= matrix, target= target))
                
        