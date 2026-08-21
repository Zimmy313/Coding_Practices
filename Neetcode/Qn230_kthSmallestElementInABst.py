# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallestSlow(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        
        def inorder(node):
            if not node:
                return 
            
            inorder(node.left)

            res.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return res[k-1]
    
    def kthSmallestFast(self, root: Optional[TreeNode], k: int) -> int:
        counter = 0
        result = None
    
        def inorder(node):
            nonlocal counter, result

            if not node or result is not None: # the second condition stops the recursive call if answer is found
                return 
            
            inorder(node.left)

            counter += 1
            if counter == k:
                result = node.val
                return 

            inorder(node.right)
        
        # This version is worth studying to learn the recursive call nature of python. 
        # It does not make use of result paramemter to capture the actual result
        # therefore, after each side need to check if result is found
        # else, by directing returning inorder(root), actual result may be replaced by None
        
        # def inorderWithoutResult(node):
        #     nonlocal counter

        #     if not node:
        #         return 
            
        #     res = inorderWithoutResult(node.left)
        #     if res in not None:
        #         return res
            
        #     counter += 1
        #     if counter == k:
        #         return node.val 

        #     return inorder(node.right)

        # return inorder(root)
        
        inorder(root)
        return result

            
