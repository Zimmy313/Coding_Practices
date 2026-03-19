from typing import *

class Solution:
    def isAnagram1(self, s: str, t: str) -> bool:
        
        result = {}
        
        for i in range(len(s)):
            if s[i] in result:
                result[s[i]] += 1
            else:
                result[s[i]] = 1
            
        for i in range(len(t)):
            if t[i] not in result:
                return False
            else:
                result[t[i]] -= 1
                if result[t[i]] == 0:
                    result.pop(t[i])
        
        subTotal = 0
        
        for value in result.values():
            subTotal += value 
        
        if subTotal == 0:
            return True 
        else:
            return False 
        
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash1 = {}
        hash2 = {}
        
        for i in s:
            if i in hash1:
                hash1[i] += 1
            else:
                hash1[i] = 1
    
        for i in t:
            if i in hash2:
                hash2[i] += 1
            else:
                hash2[i] = 1
                
        return hash1 == hash2 
        
if __name__ == "__main__":
    solver = Solution()
    s = 'anagram'
    t = 'nagaram'
    
    print(solver.isAnagram(s,t))
    
                