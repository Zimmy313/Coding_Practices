from typing import *
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        pq = []
        nope = []
        
        for i in range(len(profits)):
            if capital[i] > w:
                heapq.heappush(nope,(capital[i], profits[i]))
            else:
                heapq.heappush(pq, (-profits[i], capital[i]))
        
        while k != 0:
              
            while nope and nope[0][0] <= w: # retry past unfeasible projects
                cap, prof = heapq.heappop(nope)
                heapq.heappush(pq, (-prof, cap))
                    
            if len(pq) == 0:
                return w
                
            current = heapq.heappop(pq)    
            
            k -= 1
            w += -current[0]

        return w
            
            
            
            