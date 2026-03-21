from typing import *

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        sub_string = set()
        maximum = 0
        left = 0
        right = 0


        # move right pointer when no dup. 
        # move left pointer when there is dup. move until no dup 

        while right != len(s):
            temp_char = s[right]
        
            if temp_char not in sub_string:
                sub_string.add(temp_char)
                
                current_length = len(sub_string) # updating the maximum length
                if current_length > maximum:
                    maximum = current_length
                right += 1
                
            else:
                while left != right:
                    temp_char1 = s[left]
                    sub_string.discard(temp_char1) # removing the first element 
                    left += 1
                    
                    if temp_char not in sub_string:
                        break 
                
        return maximum
    
    def lengthOfLongestSubstring2(self, s: str) -> int: # faster. checks for the longest substring starting from all possible position
        m=0
        if s=="":
            return 0
        for i in range(len(s)):
            a=""
            j=i
            while j<len(s):
                if s[j] in a:
                    break
                a+=s[j]
                j+=1
            m=max(len(a),m) 
        return m   


if __name__ == "__main__":
    s = Solution()
    test = [
        "bbbbb"
    ]
    
    for i in range(len(test)):
        print(s.lengthOfLongestSubstring2(test[i]))



