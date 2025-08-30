from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        table = {val:idx for idx, val in enumerate(inorder)}
        self.preorder_index = 0
        
        # no slicing at all, we keep referring back to the preorder and inorder using index which we get in O(1)
        def helper(left, right):
            if left > right: # base case
                return None 
            
            root_val = preorder[self.preorder_index]
            self.preorder_index += 1
            
            root = TreeNode(root_val)
            mid = table[root_val]
            
            root.left = helper(left, mid - 1)
            root.right = helper(mid+1, right)
            
            return root
        return helper(0, len(inorder)-1)
            
            
    
    def buildTree1(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]: # slow due to slicing
        if not preorder or not inorder:
            return None
        
        root_val = preorder[0]
        mid_index = inorder.index(root_val)
        
        root = TreeNode(val = root_val)
        
        root.left = self.buildTree(preorder=preorder[1:mid_index+1], inorder = inorder[:mid_index])
        root.right = self.buildTree(preorder= preorder[mid_index+1:], inorder = inorder[mid_index+1:])
    
        
        return root
        
        
        
        
        