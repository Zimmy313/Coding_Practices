from typing import * 

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        table = {}
        table2 = {}
        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]
            
            if s_char not in table:
                table[s_char] = t_char
            
            elif s_char in table:
                
                if t_char in table[s_char]:
                    continue
                else:
                    return False
                
            if t_char not in table2:
                table2[t_char] = s_char 
            elif t_char in table2:
                if s_char in table2[t_char]:
                    continue
                else:
                    return False
        return True 
                
        