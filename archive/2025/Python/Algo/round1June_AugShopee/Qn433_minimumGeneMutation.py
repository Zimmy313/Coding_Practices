from typing import *
from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int: 
        if endGene not in bank:
            return -1
        
        q = deque()
        visited = set((startGene)) # just the node only. BFS ensures shorted path for graphs with no weight!
        bank_set = set(bank)
        letters = ['A', 'C','G','T']
        q.append((startGene, []))
        n = len(startGene)

        while q:
            current_state, sequence = q.popleft()
            if current_state == endGene: # late goal check
                return len(sequence)
            
            for i in range(n):
                current_letter = current_state[i]
                
                for letter in letters:
                    if letter == current_letter:
                        continue
                    
                    new_state = current_state[:i] + letter + current_state[i+1:]
                    
                    if new_state in bank_set and new_state not in visited:
                        visited.add(new_state)
                        new_sequence = sequence + [new_state]
                        
                        q.append((new_state, new_sequence))                    
                    
        
        return -1
