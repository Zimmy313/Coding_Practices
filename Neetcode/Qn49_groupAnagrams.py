from typing import List
from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dd = defaultdict(list)
        result = []
        
        for str in strs:
            key = tuple(sorted(Counter(str).items())) # sorting is constant as there are at most 26 characters
            dd[key].append(str)
            
        for lists in dd.values():
            result.append(lists)
            
        return result 
    
if __name__ == "__main__":
    strs = [s.strip().strip("'").strip('"') for s in input("Please input strs:\n").split(",")]
    solver = Solution()
    
    print(solver.groupAnagrams(strs))
    


                