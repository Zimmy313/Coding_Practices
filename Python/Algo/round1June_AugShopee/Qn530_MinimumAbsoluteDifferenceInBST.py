from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int: # THIS can be optimised by doing the calculation during the traversal
        self.list = []
        
        def inorder(node):
            if not node:
                return None
            
            inorder(node.left)
            self.list.append(node.val)
            inorder(node.right)
        
        inorder(root)
        result = float("inf")
        for i in range(len(self.list)-1):
            result = min(result, abs(self.list[i] - self.list[i+1]))
        return result 
        