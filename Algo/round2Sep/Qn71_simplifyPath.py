class Solution:
    def simplifyPath(self, path: str) -> str:
        pieces = path.split('/')
        stack = []

        skip = [' ', '.','']

        for piece in pieces:
            if piece in skip or (piece ==".." and len(stack) == 0):
                continue 
            
            if piece == '..' and stack:
                stack.pop()
                continue

            stack.append(piece)
        
        result = "/".join(stack)
        result = "/" + result
        
        return result