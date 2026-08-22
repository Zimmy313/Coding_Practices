"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

# consider using dfs to solve the next round

class Solution:
    def cloneGraphFirstTry(self, node: Optional['Node']) -> Optional['Node']:
        visited = set()
        reference = {}

        if not node:
            return

        q = deque([node])
        head = node.val

        while q:
            current = q.popleft()
            if current.val in visited:
                continue
            visited.add(current.val)
            
            if current.val in reference:
                copy = reference[current.val]
            else:
                copy = Node(val = current.val)
                reference[current.val] = copy
            
            for child in current.neighbors:
                q.append(child)

                if child.val in reference:
                    child_copy = reference[child.val]
                else:
                    child_copy = Node(child.val)
                    reference[child.val] = child_copy

                copy.neighbors.append(child_copy)
        
        return reference[head]


# This can be simplified by creating unseen child nodes inside the inner loop:
#
# for child in current.neighbors:
#     if child not in reference:
#         reference[child] = Node(child.val)
#         q.append(child)
#     copy.neighbors.append(reference[child])
#
# A node is added to the queue only the first time it is discovered.
# Therefore, each node is processed at most once, so a separate `visited`
# set is unnecessary.
#
# Also, if `reference` is initialized with:
#     reference = {node: Node(node.val)}
# then every node popped from the queue is guaranteed to already have
# a corresponding clone in `reference`, so we can directly use:
#     copy = reference[current]
# without an extra if-else check.

# optimised version 
    # def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    #     if not node:
    #         return None

    #     reference = {node: Node(node.val)}
    #     q = deque([node])

    #     while q:
    #         current = q.popleft()
    #         copy = reference[current]

    #         for child in current.neighbors:
    #             if child not in reference:
    #                 reference[child] = Node(child.val)
    #                 q.append(child)

    #             copy.neighbors.append(reference[child])

    #     return reference[node]
            
                
