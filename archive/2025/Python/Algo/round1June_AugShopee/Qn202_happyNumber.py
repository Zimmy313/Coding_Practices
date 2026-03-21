from typing import *

class Solution:
    def isHappy(self, n: int) -> bool:
        table = {} 
        cur_num = n 
        while True:
            counter = 0
            
            digits = []
            
            while cur_num > 0:
                digits.append(cur_num % 10)
                cur_num = cur_num // 10
            
            for num in digits:
                counter += num**2
            
            if counter == 1:
                return True 
            
            elif counter in table:
                return False 

            else:
                table[counter] = 0
                cur_num = counter
                
                
        
        
if __name__ == "__main__":
    s = Solution()
    n = 19
    print(s.isHappy(n = 19))