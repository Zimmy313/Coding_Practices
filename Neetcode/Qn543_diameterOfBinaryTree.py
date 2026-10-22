# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# The diameter of a binary tree is the maximum among the sums of the left height and right height of the nodes in the tree.
# Because the diameter of a binary tree is defined as the longest path between any two nodes in the tree. The path may or may not pass through the root. For any given node, the longest path that passes through it is the sum of the height of its left subtree and the height of its right subtree.

class Solution:
    def diameterOfBinaryTree_WRONGGG(self, root: Optional[TreeNode]) -> int:
        # this version is wrong if the longest path does not pass through the root.
        def findHeight(node):
            if not node:
                return 0

            left = 1 + findHeight(node.left)
            right = 1 + findHeight(node.right)

            return max(left, right)

        left = findHeight(root.left)
        right = findHeight(root.right)
        
        return left + right

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def findHeight(node):
            nonlocal res

            if not node:
                return 0

            left = findHeight(node.left)
            right = findHeight(node.right)

            res = max(res, left+ right)

            return max(left, right) + 1
        
        findHeight(root)
        return res