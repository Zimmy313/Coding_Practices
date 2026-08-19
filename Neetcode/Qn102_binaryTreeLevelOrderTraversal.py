# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dq = deque()
        dq.append(root)
        res = []

        while dq:

            n = len(dq)
            level = []

            for i in range(n):
                node = dq.popleft()
                
                if not node:
                    continue

                level.append(node.val)
                dq.append(node.left)
                dq.append(node.right)
            
            if level != []:
                res.append(level)
        
        return res



