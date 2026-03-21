from typing import *
from collections import Counter 

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(words[0])
        m = len(words)
        result = []
        table = Counter(words)
        
        for i in range(n): # offsets
            left = i 
            count = 0
            windoow_count = DefaultDict(int)
            
            for j in range(i, len(s) - n + 1, n):
                word = s[j:j+n]
                if word in table:
                    windoow_count[word] += 1
                    count += 1
                    
                    while windoow_count[word] > table[word]: #sliding window
                        left_word = s[left: left + n]
                        windoow_count[left_word] -= 1
                        count -= 1
                        left += n 
                    
                    if count == m:
                        result.append(left)
                else:
                    windoow_count.clear()
                    count = 0 
                    left = j+n 
        return result 
    
        
    def findSubstring1(self, s: str, words: List[str]) -> List[int]: # inefficient. TLE
        n = len(words[0])
        m = len(words)
        total_len = n*m
        
        result = []
        table = Counter(words)
        
        for i in range(len(s)-total_len + 1):
            seen = Counter()
            
            for j in range(m): # check if all words are contained
                start = i+j*n
                word = s[start:start + n]
                if word in table:
                    seen[word] += 1
                    
                    if seen[word] > table[word]:
                        break 
                else:
                    break 
            
            if seen == table:
                result.append(i)
        return result 
                
        