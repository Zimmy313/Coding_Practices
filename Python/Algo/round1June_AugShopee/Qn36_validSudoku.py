from typing import *

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool: # Will be slower then 3 passes if we use only one set. slower lookup time
        
        rows = [set() for _ in range(9)] # sacrificing spcae for time
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue

                box_index = (i // 3) * 3 + (j // 3)

                if (
                    val in rows[i] or
                    val in cols[j] or
                    val in boxes[box_index]
                ):
                    return False

                rows[i].add(val)
                cols[j].add(val)
                boxes[box_index].add(val)

        return True
    
  
    def isValidSudoku1(self, board: List[List[str]]) -> bool: # this can be imporved using a single pass
        table = set()
        
        for row in board:
            table.clear()
            for c in row:
                if c == ".":
                    continue
                
                if c in table:
                    return False
                
                table.add(c)
                
        for col in range(9):
            table.clear()
            for row in board:
                
                if row[col] == ".":
                    continue 
                if row[col] in table:
                    return False
                table.add(row[col])
        
        for col in range(0, 7, 3):
            for row in range(0, 7, 3):
                
                table.clear()
                for i in range(col, col+3):
                    for j in range(row, row+3):
                        
                        if board[i][j] == ".":
                            continue 
                        if board[i][j] in table:
                            return False 
                        table.add(board[i][j])
        return True
                                    