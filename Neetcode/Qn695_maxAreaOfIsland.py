class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        row, col = len(grid), len(grid[0])

        def dfs(i: int, j: int, area: int) -> int:
            moves = [(1,0), (0,1), (-1,0), (0,-1)]
            area += 1
            grid[i][j] = 0

            for move in moves:
                new_i = i + move[0]
                new_j = j + move[1]

                if -1 < new_i < row and -1 < new_j < col and grid[new_i][new_j] != 0:
                    area = dfs(new_i, new_j, area)
            
            return area


        for i in range(row):
            for j in range(col):

                if grid[i][j] == 0:
                    continue
                
                area = dfs(i,j, 0)
                if area > res:
                    res = area
        
        return res