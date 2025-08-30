from typing import *
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        visited = set()
        heapq.heappush(heap, (nums1[0] + nums2[0], 0,0))
        visited.add((0,0)) # visited is needed as there is 2 ways to get to a combi. e.g. to get to (2,3), you can start with (1,3) or (2,2)
        result = []
        
        
        n = len(nums1)
        m = len(nums2)
        
        while heap and len(result) < k:
            total, i ,j = heapq.heappop(heap)
            result.append((nums1[i],nums2[j]))
            
            if i+1 < n and (i+1,j) not in visited:
                heapq.heappush(heap, (nums1[i+1] + nums2[j], i+1, j))
                visited.add((i+1, j))
            
            if j+1 < m and (i,j+1) not in visited:
                heapq.heappush(heap, (nums1[i]+nums2[j+1], i, j+1))
                visited.add((i,j+1))
        return result 
            