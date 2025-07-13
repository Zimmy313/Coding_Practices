from typing import *
from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj_list = defaultdict(list)
        result = []
        
        for i in range(len(equations)): # preprocessing
            equ = equations[i]
            front = equ[0]
            back = equ[1]
            
            adj_list[front].append((back, values[i]))
            adj_list[back].append((front, 1/values[i]))
        
        for i in range(len(queries)): # main loop
            
            start = queries[i][0]
            end = queries[i][1]
            
            if start not in adj_list or end not in adj_list: # not found in adj list
                result.append(float(-1))
                continue
            
            if start == end: # edge cases
                result.append(float(1))
                continue
            
            ################## BFS
            q = deque([[start, 1]])
            visited = set()
            added = False
            
            while q and not added: # need added to stop early if result is already found
                current, current_cost = q.popleft()
                visited.add(current)
                
                
                for items in adj_list[current]:
                    next_node = items[0]
                    cost = items[1]
                    
                    if next_node not in visited:
                        new_cost = cost * current_cost
                        
                        if next_node == end:
                            result.append(new_cost)
                            added = True
                            break # breaking the inner for loop
                            
                        elif next_node in adj_list: # adding neighbours
                            q.append([next_node, new_cost])
            if added == False:
                result.append(float(-1))
        return result

    def calcEquation_DFS(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]: # Written by GPT. for study
        adj_list = defaultdict(list)
        result = []

        # Build graph
        for i in range(len(equations)):
            a, b = equations[i]
            adj_list[a].append((b, values[i]))
            adj_list[b].append((a, 1 / values[i]))

        # DFS helper function
        def dfs(current, target, visited, acc_product):
            if current == target:
                return acc_product
            visited.add(current)

            for neighbor, weight in adj_list[current]:
                if neighbor not in visited:
                    result_from_rec = dfs(neighbor, target, visited, acc_product * weight)
                    if result_from_rec != -1:
                        return result_from_rec
            return -1

        # Evaluate each query
        for start, end in queries:
            if start not in adj_list or end not in adj_list:
                result.append(-1.0)
            elif start == end:
                result.append(1.0)
            else:
                visited = set()
                result.append(dfs(start, end, visited, 1))

        return result
             
                
if __name__ == "__main__":
    s = Solution()
    equations = [["a","b"],["b","c"],["a","c"]]   
    values = [2.0,3.0,6.0]      
    queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]              
    
    print(s.calcEquation(equations, values, queries))    
                            
                    
                
            
            