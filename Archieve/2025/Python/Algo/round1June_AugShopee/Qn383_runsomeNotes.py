from typing import *

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        table = {}
        
        for char in magazine:
            
            if char in table:
                table[char] += 1
            else:
                table[char] = 1
            
        for char in ransomNote:
            if char not in table:
                return False 
            else:
                table[char] -= 1
                if table[char] <= 0:
                    table.pop(char)
        return True 
    