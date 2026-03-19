from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.postorder_index = len(postorder) - 1
        table = { val:index  for index, val in enumerate(inorder)}
        
        def helper(left, right): # left and right are pointers to the inorder array
            if left > right:
                return None

            root_val = postorder[self.postorder_index]
            root = TreeNode(val = root_val)
            self.postorder_index -= 1
            
            current_index = table[root_val]
            
            root.right = helper(current_index+1, right) # all right sub trees will be called 
            root.left = helper(left, current_index-1)
             
            
            return root 
        
        return helper(0, len(inorder) - 1)
    
    def buildTree1(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None 
        
        root = TreeNode(val = postorder[-1])
        mid = inorder.index(root.val)
        
        root.right = self.buildTree1(inorder = inorder[mid+1:], postorder=postorder[mid:-1])
        root.left = self.buildTree1(inorder=inorder[:mid], postorder=postorder[:mid])
        
        return root