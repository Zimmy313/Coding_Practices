from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for i in range(9)]
        squares = [[set() for _ in range(3)] for _ in range(3)]
        
        # handles row and cols
        for i in range(9):
            row = set()
    
            for j in range(9):
                current = board[i][j]
                
                if current == ".":
                    continue
                else:
                    current = int(current)
                    square = squares[i//3][j//3]
                    if current in row or current in cols[j] or current in square:
                        return False
                    
                    row.add(current)
                    cols[j].add(current)
                    square.add(current)
                    
        return True
    

if __name__ == "__main__":
    board = []
    print("Please input row by row")
    for i in range(9):
        row = list(input())
        board.append(row)
        
    solver = Solution()
    
    print(solver.isValidSudoku(board))

                
                
                    
        