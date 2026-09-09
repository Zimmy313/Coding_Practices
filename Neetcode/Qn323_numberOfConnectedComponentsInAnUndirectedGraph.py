from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        

        graph = [[] for _ in range(n)]
        res = 0
        seen = set()
        dq = deque()

        # building a adj list
        for edge in edges:
            a, b = edge[0], edge[1]
            graph[a].append(b)
            graph[b].append(a)
        
        for i in range(n):
            if i in seen:
                continue
            
            res += 1
            seen.add(i)
            dq.append(i)

            while dq:
                current = dq.popleft()

                for nei in graph[current]:
                    if nei not in seen:
                        seen.add(nei)
                        dq.append(nei)
            
        return res