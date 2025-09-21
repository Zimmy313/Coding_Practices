from typing import *

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None: 
        nrow = len(matrix)
        ncol = len(matrix[0])
        
        # building sets 
        for row in range(nrow):
            for col in range(ncol):
                if matrix[row][col] == 0:
                    matrix[row][col] = True
                    
        for row in range(nrow):
            for col in range(ncol):
                
                if matrix[row][col] is True:
                    
                    # change the columns
                    for j in range(ncol):
                        if matrix[row][j] is True:
                            continue 
                        else:
                            matrix[row][j] = 0
                    
                    
                    # change the rows
                    for i in range(nrow):
                        if matrix[i][col] is True:
                            continue
                        else:
                            matrix[i][col] = 0
                    matrix[row][col] = 0
        return 
                    
        
    def setZeroes1(self, matrix: List[List[int]]) -> None: # not friendly with sapce
        """
        Do not return anything, modify matrix in-place instead.
        """
        nrow = len(matrix)
        ncol = len(matrix[0])
        row_table = set()
        col_table = set()
        
        # building sets 
        for row in range(nrow):
            for col in range(ncol):
                if matrix[row][col] == 0:
                    row_table.add(row)
                    col_table.add(col)
        
        # in-place modification
        for row in row_table:
            for col in range(ncol):
                 matrix[row][col] = 0
        
        for col in col_table:
            for row in range(nrow):
                matrix[row][col] = 0
        return         
                
                
        
if __name__ == "__main__":
    solver = Solution()
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    print(solver.setZeroes(matrix))      