from typing import *
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth_DFS(self, root: Optional[TreeNode]) -> int: 
        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        return 1 + max(left, right)
    
    def maxDepth_BFS(self, root: Optional[TreeNode]) -> int: 
        if not root:
            return 0
        
        q = deque([root])
        counter = 0
        
        while q:
            level_size = len(q)
            counter += 1
            for i in range(level_size):
                current = q.popleft()
                
                if current.right is not None:
                    q.append(current.right)
                    
                if current.left is not None:
                    q.append(current.left)
            
        return counter 
    
                
        