from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q: # both reaching the end
            return True
        
        if (p is None and q is not None) or (p is not None and q is None): # different structure
            return False 
        
        if p.val != q.val:
            return False
        
        if p.val == q.val: # same value
            left_result = self.isSameTree(p.left, q.left)
            right_result = self.isSameTree(p.right, q.right)
        
        return left_result and right_result
        
        