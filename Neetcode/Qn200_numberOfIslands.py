class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        row, col = len(grid), len(grid[0])

        def dfs(i,j):
            moves = [(0, 1), (0, -1), (1, 0), ( -1, 0)]

            for move in moves:
                new_i = i + move[0]
                new_j = j + move[1]

                if 0 <= new_i < row and 0 <= new_j < col:
                    if grid[new_i][new_j] == "0":
                        continue
                    grid[new_i][new_j] = "0"
                    dfs(new_i, new_j)
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    result += 1
                    dfs(i,j)

        return result


                        
