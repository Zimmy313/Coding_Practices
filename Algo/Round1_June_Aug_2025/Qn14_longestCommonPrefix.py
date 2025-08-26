from typing import *

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        base = strs[0]
        
        for word in strs[1:]:
            
            while not word.startswith(base):
                base = base[:-1]
                
                if base == "":
                    return ""
        return base 