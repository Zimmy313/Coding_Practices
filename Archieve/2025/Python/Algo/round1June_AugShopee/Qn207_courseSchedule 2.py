from typing import *
from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True
        
        graph = defaultdict(list)
        degree = [0] * numCourses
        q = deque()
        counter = 0
        for combi in prerequisites: # building adjacency list and populate the degree counter 
            course, pre = combi 
            graph[pre].append(course)
            degree[course] += 1
        
        for i in range(numCourses): # initialising the q
            if degree[i] == 0:
                q.append(i)
        
        while q:
            current = q.popleft()
            counter += 1
            
            for neighbour in graph[current]:
                degree[neighbour] -= 1
                
                if degree[neighbour] == 0:
                    q.append(neighbour)
        
        return True if numCourses == counter else False 
    
if __name__ == "__main__":
    s = Solution()
    numCourses = 2
    prerequisites = [[0,1]]
    print(s.canFinish(numCourses, prerequisites))
            

            