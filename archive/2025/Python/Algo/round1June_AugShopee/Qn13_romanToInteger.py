from typing import *

class Solution:
    def romanToInt(self, s: str) -> int:
        table = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        result = 0
        temp = 0
        pre_char = None
        
        for char in s:
            
            if pre_char == None or pre_char == char:
                temp += table[char]
                pre_char = char
                
            elif table[pre_char] < table[char]: # need to deduct
                temp = table[char] - temp 
                result += temp
                temp = 0
                pre_char = char 
            else:
                result += temp
                temp = table[char]
                pre_char = char 
        result+=temp
        return result 
    
if __name__ == "__main__":
    solver = Solution()
    s = "MCMXCIV"
    print(solver.romanToInt(s))
                