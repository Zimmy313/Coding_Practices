from typing import *

class Solution:
    def isPalindrome(self, s:str) -> bool:


        length = len(s)
        converted = []

        for i in range(length):
        
            if not s[i].isalnum() :
                continue 
            elif s[i].isupper():
                converted.append(s[i].lower())
            else:
                converted.append(s[i])

        len2 = len(converted)

        if len2 == 0 :
            return True 

        p1 = 0
        p2 = len2 - 1
        
        while p1 < p2:
            if converted[p1] != converted[p2]:
                return False 
            p1 += 1
            p2 -= 1
        return True 

if __name__ == "__main__":
    s = Solution()
    test = "A man, a plan, a canal: Panama"
    print(s.isPalindrome(test))