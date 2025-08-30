from collections import deque
from typing import *

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        degrees = [0] * numCourses 
        q = deque()
        result = []

        # graph building 
        for course, pre in prerequisites:
            graph[pre].append(course)
            degrees[course] += 1

        # initialise the q
        for i in range(numCourses):
            if degrees[i] == 0:
                q.append(i)

        while q: 
            current = q.popleft()
            result.append(current)

            for course in graph[current]:
                degrees[course] -= 1
                if degrees[course] == 0:
                    q.append(course)
        return result if len(result) == numCourses else []
        
# when creating list or matrix
# use * only when the elements are immutable(e.g. int,float,None,str, etc). Do not use it for mutable objects
# use [[] for _ in range()] when the elements are mutable(e.g. list,dict,set, etc)
