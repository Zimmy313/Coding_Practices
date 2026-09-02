from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # adj list
        graph = [[] for _ in range(numCourses)]
        # indegree for khan's
        indegree = [0] * numCourses
        res = 0

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        dq = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                dq.append(i)
                indegree[i] = -1
        
        while dq:
            current = dq.popleft()
            res += 1

            for node in graph[current]:
                indegree[node] -= 1

                if indegree[node] == 0:
                    dq.append(node)
                    indegree[node] = -1 
            
        return res == numCourses

