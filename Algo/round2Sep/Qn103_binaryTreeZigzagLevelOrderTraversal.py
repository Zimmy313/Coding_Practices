from typing import *
from collections import deque 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque([])
        q.append(root)
        reverse = True
        result = []
        
        while q:
            count = len(q)
            temp = []
            
            if reverse:
                for i in range(count):
                    node = q.pop()
                    temp.append(node.val)
                    if node.left: q.appendleft(node.left)
                    if node.right:q.appendleft(node.right)
                reverse = False 
            
            else:
                for i in range(count):
                    node = q.popleft()
                    temp.append(node.val)
                    if node.right:q.append(node.right)
                    if node.left: q.append(node.left)
                    
                reverse = True 
            result.append(temp)
        return result 
                    
                    
                        
                
        
        