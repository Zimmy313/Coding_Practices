class CodecUniqueOnly:
# this solution assumes node.val's are all unique. else it wont work
    def serialize(self, root: Optional[TreeNode]) -> str:
        inorder = []
        preorder = []

        def get_inorder(node):
            if not node:
                return

            get_inorder(node.left)
            inorder.append(str(node.val))
            get_inorder(node.right)

        def get_preorder(node):
            if not node:
                return

            preorder.append(str(node.val))
            get_preorder(node.left)
            get_preorder(node.right)

        get_inorder(root)
        get_preorder(root)

        return ",".join(inorder) + "|" + ",".join(preorder)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        inorder_str, preorder_str = data.split("|")

        if not inorder_str:
            return None

        inorder = inorder_str.split(",")
        preorder = preorder_str.split(",")

        hashmap = {
            value: i
            for i, value in enumerate(inorder)
        }

        preorder_i = 0

        def helper(left, right):
            nonlocal preorder_i

            if left > right:
                return None

            root_val = preorder[preorder_i]
            preorder_i += 1

            root = TreeNode(int(root_val))

            mid_index = hashmap[root_val]

            root.left = helper(left, mid_index - 1)
            root.right = helper(mid_index + 1, right)

            return root

        return helper(0, len(inorder) - 1)
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return 
            
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")
        i = 0

        def dfs():
            nonlocal i 

            if values[i] == "N":
                i += 1
                return None
            
            node = TreeNode(int(values[i]))
            i += 1

            node.left = dfs()
            node.right = dfs()

            return node
        
        return dfs()
