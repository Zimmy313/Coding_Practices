from typing import *

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = nums[:k]
        heapq.heapify(pq)
        
        for num in nums[k:]:
            heapq.heappushpop(pq, num)
            
        return pq[0]