# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")

        def dfs(node):
            nonlocal res

            if not node:
                return 0

            left = dfs(node.left)
            left = max(left, 0)

            right = dfs(node.right)
            right = max(right, 0)

            mid = node.val

            res = max(mid+left+right, res)
            return mid + max(left,right)

        dfs(root)
        return res
        
        





