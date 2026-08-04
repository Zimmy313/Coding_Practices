class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }

        stack = []

        for char in s:
            if char in "({[":
                stack.append(char)
            
            else:
                if not stack:
                    return False
                
                top = stack.pop()

                if pairs[top] != char:
                    return False

        return len(stack) == 0 # catch missing parenthesis. cant just return true


                
                
