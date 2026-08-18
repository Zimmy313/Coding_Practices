# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False

        if self.sameTree(root, subRoot):
            return True
        
        return (
            self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        )


    def sameTree(self, p, q):
        if p is None and q is None:
            return True
        
        if p is None or q is None:
            return False
        
        if p.val != q.val:
            return False
        
        return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)
            



        # if (root is None and subRoot is not None) or (root is not None and subRoot is None):
        #     return False
        # if root is None and subRoot is None:
        #     return True

        
        # if root.val != subRoot.val:
        #     return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        # elif root.val == subRoot.val:
        #     return (self.isSubtree(root.left, subRoot.left) and self.isSubtree(root.right, subRoot.right)) or (
        #         self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        #     )

        