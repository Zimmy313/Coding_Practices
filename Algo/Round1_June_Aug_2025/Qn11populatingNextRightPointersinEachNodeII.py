from typing import *
from collections import deque 


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q = deque([root])
        
        while q:
            n = len(q)
            pre = None
            
            for i in range(n):
                current = q.popleft()
                if pre is not None:
                    pre.next = current
                pre = current 
                
                    
                
                if current.left != None:
                    q.append(current.left)
                if current.right != None:
                    q.append(current.right)
            if pre is not None:
                pre.next = None 
        return root 

        