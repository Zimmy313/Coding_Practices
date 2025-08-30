from typing import List 

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = matrix[0] # rows
        m = matrix[0][0] # cols
        col = set()
        row = set()
        
        # need to first scan the matrix to find the rows and columns to be zeroed
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    col.add(j)
                    row.add(i)
                    
                
        
        