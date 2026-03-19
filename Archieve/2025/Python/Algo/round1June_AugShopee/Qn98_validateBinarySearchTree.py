from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 
        
        result = []
        
        def inorder(node):
            nonlocal result 
            if not node:
                return 
            
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        
        inorder(root)
            
        for i in range(len(result)-1):
            if result[i] >= result[i+1]:
                return False
        return True