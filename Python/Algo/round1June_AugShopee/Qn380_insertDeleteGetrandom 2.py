import random

class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.num = []
        

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False 
        self.dict[val] = len(self.num)
        self.num.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.dict:
            pos = self.dict[val]
            last_val = self.num[-1]

            # placing last num to the current pos
            self.num[pos] = last_val
            self.dict[last_val] = pos 

            self.dict.pop(val)
            self.num.pop()
            return True 
        return False
        
        

    def getRandom(self) -> int:
        return random.choice(self.num)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()