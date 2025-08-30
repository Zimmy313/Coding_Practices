from typing import *
from collections import deque
import numpy as np

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])
        result = []
        
        while q:
            level_size = len(q)
            temp = []
            
            for i in range(level_size):
                current = q.popleft()
                temp.append(current.val)
                
                if current.left is not None:
                    q.append(current.left)
                if current.right is not None:
                    q.append(current.right)
            
            result.append(np.mean(temp))
        return result 
    
            
        
