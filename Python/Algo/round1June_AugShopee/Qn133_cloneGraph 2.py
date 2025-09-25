
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
from collections import deque 

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited = {} # node : copy of node
        q = deque([node])
        
        while q:
            current = q.popleft()
            
            if current not in visited:
                new_node = Node(val = current.val)
                visited[current] = new_node # mark as visited
            
            for neighbor in current.neighbors: # add all neighbors of the current node
                if neighbor not in visited:
                    q.append(neighbor)
                    visited[neighbor] = Node(val = neighbor.val)
                
                visited[current].neighbors.append(visited[neighbor])
        return visited[node]
    
                    
            
            
        
        
        
        