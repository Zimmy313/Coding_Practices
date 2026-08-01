class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []
        self.pointer = -1

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.pointer == -1 :
            self.minimum.append(val)
            self.pointer += 1
        else:
            self.minimum.append(min(val, self.minimum[self.pointer]))
            self.pointer += 1
        
    def pop(self) -> None:
        self.stack.pop()
        self.minimum.pop()
        self.pointer -= 1

    def top(self) -> int:
        return self.stack[self.pointer]
        

    def getMin(self) -> int:
        return self.minimum[self.pointer]
        
