from typing import *

class Solution:
    def intToRoman(self, num: int) -> str:
        table = {
            1 : "I",
            5 : "V",
            10 : "X",
            50 : "L",
            100 : "C",
            500 : "D",
            1000 : "M"
        }
        
        n = len(str(num))
        digits = []
        remainder = num
        
        for i in range(n-1, -1, -1):
            current = remainder // (10**i) # floor division 
            remainder = remainder % (10**i) # getting the remainders
            digits.append(current) 
        
        result = ''
        
        for i in range(n-1, -1, -1): # index will show the magnitude of the current digit
            current_digit = digits[n-1-i]
            magnitude = 10**i
            
            if current_digit == 0:
                continue 
            
            elif current_digit < 4 :
                result += table[magnitude] * current_digit
            
            elif current_digit == 4:
                result += table[magnitude] + table[5 * magnitude]

            elif current_digit == 5:
                result += table[magnitude * 5]
            
            elif current_digit in [6,7,8]:
                result += table[magnitude * 5] + table[magnitude] * (current_digit-5)
            
            elif current_digit == 9:
                result += table[magnitude] + table[magnitude*10]
        
        return result 
                
                
if __name__ == "__main__":
    s = Solution()
    num = 3749
    print(s.intToRoman(num))
                
                
                

                
                            
            
            
        
         
    