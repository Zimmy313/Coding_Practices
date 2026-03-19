from typing import *

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        result = [intervals[0]]
        counter = 0 # points at the location in result
        
        for i in range(1, len(intervals)): # in each iteration, we always compare foward, see if we can merge to the previous interval
            
            current = intervals[i]
            pre = result[counter]
            
            if current[0] <= pre[1]: # overlaps
                new = [pre[0], max(current[1], pre[1])]
                result.pop()
                result.append(new)
            
            else: # no overlap
                counter += 1
                result.append(current)
        
        return result

if __name__ == "__main__":
    s = Solution()
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(s.merge(intervals))
                
            
            
            