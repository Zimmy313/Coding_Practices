from typing import *

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        counter = 0
        n = len(intervals)
        
        while counter < n and intervals[counter][1] < newInterval[0]:
            result.append(intervals[counter])
            counter += 1
            
        while counter < n and intervals[counter][0] <= newInterval[1]:
            newInterval[0] = min(intervals[counter][0], newInterval[0])
            newInterval[1] = max(intervals[counter][1], newInterval[1])
            counter += 1
        
        result.append(newInterval)
        
        while counter < n:
            result.append(intervals[counter])
            counter += 1
        return result 
            
        
        
        
        
        
        
        
        
        
        
        
        
        for i in range(len(intervals)):
            
            if intervals[i][1] >= newInterval[0]:
                
                if intervals[i][0] > newInterval[1]: # no need to merge
                    result.append(newInterval)
                    result.append(intervals[i])
                    
                else:
                    
                    
                    new = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
                    result.append(new)
                    break 
        
        
        
        
                
        
        