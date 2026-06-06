from collections import Counter, defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dd = defaultdict(list)
        result = []
        n = len(nums)
        counter = k
        
        counts = Counter(nums)
        
        for key, value in counts.items():
            dd[value].append(key)
            
        while counter != 0: 
            current = dd[n]
            
            if len(current) == 0:
                n -= 1
                continue
            
            result += current 
            counter -= len(current)
            n -= 1
            
        return result 
    
if __name__ == "__main__":
    nums = list(map(int, input("Please input nums:\n").split(",")))
    k = int(input("Please input k:\n"))
    
    solver = Solution()
    
    print(solver.topKFrequent(nums, k))
    
            