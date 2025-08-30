from typing import *

class Solution:
    def DFS(self, row, col, grid):
        stack = [(row, col)]
        
        moves = [(0,1), (0,-1), (1,0), (-1,0)]
        
        while stack:
            current = stack.pop()
            
            for move in moves:
                row1 = move[0] + current[0]
                col1 = move[1] + current[1]
                
                if 0 <= row1 < len(grid) and 0 <= col1 < len(grid[0]) and grid[row1][col1] != '0': # valid positions
                    grid[row1][col1] = '0'
                    stack.append((row1,col1))                
            
    
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        for i in range(len(grid)):
            
            for j in range(len(grid[0])):
                
                if grid[i][j] != '0':
                    self.DFS(row = i, col = j, grid = grid)
                    counter += 1
        return counter 
                
                
                