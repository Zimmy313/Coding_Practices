from typing import *
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool: 
        q = deque([root])

        while q:
            level_size = len(q)
            level = []

            for i in range(level_size):
                current = q.popleft()
                current_val = None if current is None else current.val
                level.append(current_val)
                if current is not None:
                    q.append(current.left)
                    q.append(current.right)

            if len(level) == 1:
                continue

            mid = len(level) // 2 
            left = level[:mid]
            right = level[mid:]
            right.reverse()
            if left != right:
                return False 
        return True

# This approach works because I included None into the level array. Fails if I remove it. 
# Another approach using BST is using pairs for each entry: e.g. 

#  q = deque([(root.left, root.right)])

#         while q:
#             left, right = q.popleft()

#             if not left and not right:
#                 continue
#             if not left or not right:
#                 return False
#             if left.val != right.val:
#                 return False

#             # Enqueue mirrored children
#             q.append((left.left, right.right))
#             q.append((left.right, right.left))

# alternatively, do traversal in both side. Left side in order. right side reverse of in order