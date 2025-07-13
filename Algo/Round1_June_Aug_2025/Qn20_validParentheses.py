from typing import *
from collections import deque 

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        
        left = ["(", "{", "["]
        
        for char in s:
            
            if char in left:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                
                match = stack.pop()
                
                if char == ")":
                    if match == "(":
                        continue 
                    else:
                        return False
                    
                elif char == "]":
                    if match == "[":
                        continue 
                    else:
                        return False
                else:
                    if match == "{":
                        continue 
                    else:
                        return False
        return True if len(stack) == 0 else False
                    
                        
        



if __name__ == "__main__":
    solver = Solution()
    s = "()"
    
    print(solver.isValid(s))