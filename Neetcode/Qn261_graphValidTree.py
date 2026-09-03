# Properties of a Tree (undirected graph):
# - No cycles
# - Fully connected
# - |E| = |V| - 1
#
# Any TWO of the above imply the third, and are sufficient to prove it is a tree.
from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        seen = set()
        graph = [ [] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # check for fully connectedness
        dq = deque()
        dq.append(0)
        seen.add(0)

        while dq:
            current = dq.popleft()
            neighbors = graph[current]

            for nei in neighbors:
                if nei in seen:
                    continue
                
                dq.append(nei)
                seen.add(nei)
        
        if n-1 == len(edges) and n == len(seen):
            return True
        
        return False
        
        
        
