# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
from typing import *
from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque([root])
        result = []
        
        while q:
            size = len(q)
            temp = []
            for _ in range(size):
                
                current = q.popleft()
                temp.append(current.val)
                
                if current.left is not None:
                    q.append(current.left)
                
                if current.right is not None:
                    q.append(current.right)
            result.append(temp)
        
        return result 
        

