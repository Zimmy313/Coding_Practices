from typing import *

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = 0
        flag = False
        
        for i in range(len(s)-1, -1, -1):
            char = s[i]
            
            if char == " " and flag == False:
                continue
            elif char != " ":
                if flag == False:
                    flag = True 
                result += 1
            elif char == " " and flag == True:
                break 
        return result 