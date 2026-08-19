class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board[0]), len(board)
        visited = set()

        def dfs(i, j, index):
            visited.add((i,j))

            if word[index] == board[i][j]:
                if index == len(word) - 1:
                    return True
                else:
                    moves = [(0,1), (1,0), (-1,0), (0,-1)]
                    found = []
                    for move in moves:
                        new_i = i + move[0]
                        new_j = j + move[1]

                        if 0 <= new_i < n and 0 <= new_j < m and (new_i,new_j) not in visited:
                            found.append(dfs(new_i, new_j, index + 1))
            else:
                visited.remove((i,j))
                return False
                            
            visited.remove((i,j))
            return any(found)

        for i in range(n):
            for j in range(m):
                if dfs(i,j,0):
                    return True

        return False