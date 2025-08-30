from typing import *

class MinStack:

    def __init__(self):
        self.stack = [] # each element will be a tuple (val, min_at_push)
        self.min = float("inf")
        

    def push(self, val: int) -> None:
        self.min = min(self.min, val)
        self.stack.append((val, self.min))
        
    def pop(self) -> None:
        
        temp = self.stack.pop()
        
        if len(self.stack) == 0:
            self.min = float("inf")
        else:
            if temp[1] < self.stack[-1][1] :
                self.min = self.stack[-1][1]
        
    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]