from typing import *
from collections import deque

class Solution:
    def reverseWords(self, s: str) -> str: # 2 pointers O(1) space complexity
        s = s.split() # returns a list where words are separated by white spaces
        
        left, right = 0 , len(s)-1
        
        while left < right:
            s[right], s[left] = s[left], s[right]
            left += 1
            right -= 1
        
        return " ".join(s)
        
        
        
    def reverseWords1(self, s: str) -> str: 
        temp = ""
        result = deque()
        
        for i in range(len(s)):
            char = s[i]
            
            if  char == " ":
                if temp == "":
                    continue
                else:
                    result.appendleft(temp)
                    temp = ""
            else:
                temp = temp + char
        if temp != "":
            result.appendleft(temp)
                
        result2 = ""
        
        for i in range(len(result)-1):
            word = result[i]
            result2 = result2 + word
            result2 = result2 + " "
        result2 = result2 + result[len(result)-1]
        return result2 
    
if __name__ == "__main__":
    solver = Solution()
    s = "  hello world  "
    print(solver.reverseWords(s))
    
                    
            
            
            
            