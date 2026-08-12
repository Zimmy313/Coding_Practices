# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0

        result = 1

        def helper(node, result):
            if not node:
                return result

            result += 1

            left = helper(node.left, result)
            right = helper(node.right, result)

            return max(left, right)

        result_left = helper(root.left, result)
        result_right = helper(root.right, result)

        return max(result_left, result_right)

