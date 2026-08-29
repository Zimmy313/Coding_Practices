class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        atlantic = set()
        pacific = set()
        res = []

        
        def dfs(x,y, visited):
            visited.add((x,y))

            moves = [(1,0), (0,1), (-1,0), (0,-1)]

            for move in moves:
                new_x = move[0] + x
                new_y = move[1] + y

                if new_x < 0 or new_x >= row or new_y < 0 or new_y >= col or (new_x, new_y) in visited:
                    continue

                if heights[x][y] <= heights[new_x][new_y]:
                    visited.add((new_x, new_y))
                    dfs(new_x, new_y, visited)
        
        for i in range(col):
            pacific.add((0, i))
            dfs(0,i, pacific)

            atlantic.add((row - 1, i))
            dfs(row - 1, i, atlantic)
        
        for j in range(row):
            pacific.add((j, 0))
            dfs(j, 0, pacific)

            atlantic.add((j, col - 1))
            dfs(j, col - 1, atlantic)
        
        for pair in atlantic:
            if pair in pacific:
                res.append([pair[0], pair[1]])
            
        return res