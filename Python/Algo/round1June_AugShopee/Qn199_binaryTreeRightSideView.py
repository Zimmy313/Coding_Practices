from typing import *
from collections import deque 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = deque([root])
        result = []
        
        while q:
            n = len(q)
            
            for i in range(n):
                current = q.popleft()
                
                if i == n-1:
                    result.append(current.val)
                    
                if current.left: q.append(current.left)
                if current.right: q.append(current.right)
        return result 
                
                
        