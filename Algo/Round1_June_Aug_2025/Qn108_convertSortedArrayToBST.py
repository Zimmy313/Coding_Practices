
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import *

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return []
        
        mid = len(nums) // 2
        
        root = TreeNode(val = nums[mid])
        root.left = self.sortedArrayToBST(nums = nums[:mid])
        root.right = self.sortedArrayToBST(nums = nums[mid+1:])
        
        return root 
        