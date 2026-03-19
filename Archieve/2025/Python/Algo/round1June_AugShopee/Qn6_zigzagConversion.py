from typing import *


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) == 1:
            return s
        
        matrix = [''] * numRows 
        current_row = 0
        up = False
        for i in range(len(s)):
            char = s[i]
            
            if not up:
                
                if current_row != numRows - 1:
                    matrix[current_row] = matrix[current_row] + char 
                    current_row += 1
                
                elif current_row == numRows - 1:
                    matrix[current_row] = matrix[current_row] + char 
                    up = True 
                    current_row -= 1
            
            else:
                if current_row != 0:
                    matrix[current_row] = matrix[current_row] + char 
                    current_row -= 1
                elif current_row == 0:
                    matrix[current_row] = matrix[current_row] + char 
                    up = False
                    current_row += 1
        return "".join(matrix)


        
        
        