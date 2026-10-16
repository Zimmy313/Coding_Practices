class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        n = len(intervals)
        counter = 0

        while counter < n and intervals[counter][1] < newInterval[0]:
            res.append(intervals[counter])
            counter += 1
        
        # check if overlap
        while counter < n and intervals[counter][0] <= newInterval[1]:
            newInterval[0] = min(intervals[counter][0], newInterval[0])
            newInterval[1] = max(intervals[counter][1], newInterval[1])
            counter += 1
        
        res.append(newInterval)

        while counter < n:
            res.append(intervals[counter])
            counter += 1

        
        return res
        
        

