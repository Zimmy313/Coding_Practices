from typing import *

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        
        words = s.split(" ")
        table = {}
        sets = set()
        
        if len(pattern) != len(words):
            return False
        
        for i in range(len(words)):
            char = pattern[i]
            word = words[i]
            
            if char in table:
                if table[char] == word:
                    continue 
                
                else:
                    return False 
            
            else:
                if word in sets:
                    return False
                table[char] = word 
                sets.add(word)
        return True 