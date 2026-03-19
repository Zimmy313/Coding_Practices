from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        
        pre = None 
        
        # pre-order traversal
        def preOrder(node):
            nonlocal pre
            
            if not node:
                return

            preOrder(node.right)
            preOrder(node.left)
            
            node.left = None 
            node.right = pre 
            pre = node 

        preOrder(root)