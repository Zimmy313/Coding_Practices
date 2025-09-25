from typing import *

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # Sort by the end coordinate
        points.sort(key=lambda x: x[1])

        arrows = 1
        arrow_pos = points[0][1]
        
        for x_start, x_end in points[1:]: # this is ok as you are sorting base on x_end. meaning that previous end is smaller than the next.
            if x_start > arrow_pos:
                arrows += 1
                arrow_pos = x_end
        return arrows
        
    def findMinArrowShots1(self, points: List[List[int]]) -> int: # highly inefficient due to pop(0)
        points.sort(key = lambda x:x[0])
        first = points.pop(0)
        result = [first]
        
        while points:
            next = points.pop(0)
            pre = result.pop()
            
            if pre[1] >= next[0]:
                new = [next[0], min(pre[1], next[1])]
                result.append(new)
                
            else:
                result.append(pre)
                result.append(next)
        
        return len(result)
        