from typing import List

class Solution:
    
    def encode(self, strs: List[str]) -> str:
        result = []
        n = len(strs)
        
        for i in range(n):
            m = len(strs[i])
            temp = str(m) + "#"
            
            result.append(temp)
            result.append(strs[i])
        
        final_res = "".join(result)
        
        return final_res
            

    def decode(self, s: str) -> List[str]:
        result = []
        p = 0
        n = len(s)
        
        while p < n:
            q = p
            
            while s[q] != "#":
                q += 1
            
            length = int(s[p:q])
            
            current = s[q+1:q+length+1]
            result.append(current)
            
            p = q+length+1
            
            
        
        return result


if __name__ == "__main__":
    
    strs = list(map(str, input("Please input strs:\n").split(",")))
    
    solver = Solution()
    
    coded = solver.encode(strs)
    print(coded)
    
    decoded = solver.decode(coded)
    print(decoded)
        
    