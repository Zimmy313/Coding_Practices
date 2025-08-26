from typing import * 

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class BSTIterator:
    
    
    def __init__(self, root: Optional[TreeNode]):
        self.pointer = -1
        self.result = []
        
        def inorder(node):
            if not node:
                return 
            
            inorder(node.left)
            self.result.append(node.val)
            inorder(node.right)
        
        inorder(root)
        
        self.n = len(self.result)

    def next(self) -> int:
        self.pointer += 1
        
        return self.result[self.pointer]
        

    def hasNext(self) -> bool:
        return True if self.pointer+1 < self.n else False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()