from typing import *
import heapq

class MedianFinder:

    def __init__(self):
        self.min_heap = [] # for bigger half
        self.max_heap = [] # for smaller half
        

    def addNum(self, num: int) -> None:
        if (len(self.max_heap) + len(self.min_heap)) == 0:
            heapq.heappush(self.max_heap, -num)

        # choose side to insert
        else:
            small = -self.max_heap[0]
            if num <= small:
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)
                
            
            while abs(len(self.min_heap) - len(self.max_heap)) > 1: # need rebalance
                if len(self.max_heap) > len(self.min_heap) + 1:
                    move = -heapq.heappop(self.max_heap)
                    heapq.heappush(self.min_heap, move)
                else:
                    move = -heapq.heappop(self.min_heap)
                    heapq.heappush(self.max_heap, move)
            
            

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        elif len(self.max_heap)< len(self.min_heap):
            return self.min_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()