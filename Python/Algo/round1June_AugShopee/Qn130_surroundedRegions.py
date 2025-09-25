from typing import *

class Solution:
    def DFS(self, x, y, board, visited):
        m = len(board)
        n = len(board[0])
        moves = [(0,1), (0,-1), (1,0), (-1,0)]
        
        stack = []
        stack.append((x,y))
        result = []
        
        change = True # assuming it is surrounded
        
        
        while stack:
            
            current = stack.pop()
            result.append((current))
            
            if current[0] == 0 or current[0]== m-1 or current[1] == 0 or current[1] == n-1:
                change = False 
            
            for move in moves:
                new_x= current[0] + move[0]
                new_y= current[1] + move[1] 
                
                if 0 <= new_x < m and 0 <= new_y < n and visited[new_x][new_y] != 1: # valid position
                    
                    if board[new_x][new_y] == "X":
                        visited[new_x][new_y] = 1 # help to skip step in main
                    
                    else: # position == "O"
                        visited[new_x][new_y] = 1
                        stack.append((new_x,new_y))
                        
                        
                            
        return [change, result]
                        
                        

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 1. DFS flood fill once O is encountered.
        # While doing the floodfill, keep note if it is trapped ==> is there any cell that is in the boundary
        # if no, convert to X. else, dont.
        m = len(board)
        n = len(board[0])
        
        visited = [[0]*n for _ in range(m)] # 0 means not visited. 1 means visited
        
        
        for i in range(m):
            for j in range(n):
                
                if visited[i][j] == 1:
                    continue 
                
                elif board[i][j] == "X":
                    visited[i][j] = 1
                
                else:
                    change, result = self.DFS(i,j,board, visited)
                    
                    if change:
                        for x,y in result:
                            board[x][y] = "X"
                
                
                