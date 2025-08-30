from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = []
        s = ""
        
        def dfs(node, s):
            nonlocal result 
            
            s += str(node.val)
            
            if node.left is None and node.right is None:
                result.append(int(s))
                return
            
            if node.left:
                dfs(node.left, s)
            if node.right:
                dfs(node.right, s)
                
        dfs(root, s)
        
        return sum(result)
            
        
            
            