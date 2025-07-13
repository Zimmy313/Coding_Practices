from typing import *

class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        if not ratings:
            return 0
        
        result = [1] * len(ratings)
        
        # forward pass
        for i in range(1, len(ratings)): # you check with the previous one which we are more certain. i.e. already checked in previous round
            # since you are not certain about result[0], it is the need we need 2 passes.
            if ratings[i] > ratings[i-1]:
                result[i] = result[i-1] + 1

        # backward pass
        for i in range(-2, -len(ratings)-1, -1):
            if ratings[i] > ratings[i+1]:
                result[i] = max(result[i], result[i+1] + 1) # need to check if it is alr bigger, else we will break what we have from previous pass.
                # max replaces the need to check if result[i] > result[i+1]
                # e.g. ratings = [1, 3, 4, 5, 2]. breaks if no max

                
        return sum(result)
        
    def candy1(self, ratings: List[int]) -> int: # brute force TLE
        result = [1] * len(ratings)
        changed = True
        
        if not ratings:
            return 0
        
        if len(ratings) == 1:
            return 1
        
        while changed:
            changed = False
            for i in range(len(ratings)):
                
                if i == 0:
                    if ratings[i] > ratings[i+1] and result[i] <= result[i+1]:
                        result[i] = result[i+1] + 1
                        changed = True
                
                elif i == len(ratings) -1 :
                    if ratings[i] > ratings[i-1] and result[i] <= result[i-1]:
                        result[i] = result[i-1]  + 1
                        changed = True
                
                else:
                    if ratings[i] > ratings[i+1] and result[i] <= result[i+1]:
                        result[i] = result[i+1]  + 1
                        changed = True
                    if ratings[i] > ratings[i-1] and result[i] <= result[i-1]:
                        result[i] = result[i-1]  + 1
                        changed = True
        return sum(result)
    
    



if __name__ == "__main__":
    solver = Solution()
    ratings =[1,0,2]
    print(solver.candy(ratings))