# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        isBalanced = True
        
        def findHeight(node, height):
            nonlocal isBalanced 

            if not node:
                return height
            
            
            left = findHeight(node.left, height + 1)
            right = findHeight(node.right, height + 1)

            if abs(left - right) > 1:
                isBalanced = False

            return max(left, right)
        
        findHeight(root, 0)

        return isBalanced
        

        
