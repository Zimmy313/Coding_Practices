from typing import *


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for str in strs:
            temp = []
            
            for c in str:
                temp.append(c)
            
            temp.sort()
            temp_str = "".join(temp)
            
            if temp_str not in result:
                result[temp_str] = [str]
            else:
                result[temp_str].append(str)
        
        final_result = []
        
        for value in result.values():
            final_result.append(value)
        
        return final_result

if __name__ == "__main__":
    solver = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(solver.groupAnagrams(strs))
                