from typing import *

class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        num = 0
        sign = 1
        stack = []

        for c in s:
            if c == " ":
                continue

            elif c.isnumeric():
                num = num*10 + int(c) # building number 
            
            elif c == "+":
                res += num*sign
                num = 0
                sign = 1

            elif c == "-":
                res += num*sign 
                num = 0
                sign = -1
            
            elif c == "(":
                res += num*sign
                stack.append((res, sign))
                res = 0
                sign = 1
            
            elif c == ")":
                res += num*sign 
                prev_res, prev_sign = stack.pop()
                res = prev_res + prev_sign * res
                num = 0
                
                
        res += num*sign
        return res 


if __name__ == "__main__":
    solver = Solution()
    s =  " 2-1 + 2 "
    print(solver.calculate(s))
                            
                    
                    
                    