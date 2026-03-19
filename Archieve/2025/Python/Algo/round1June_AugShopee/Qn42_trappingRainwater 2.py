from typing import *

class Solution:
    def trap(self, height: List[int]) -> int: # 3 passes. there can be a more efficient way to handle this using a single pass.
        
        left_max = [0 for i in range(len(height))]
        right_max = [0 for i in range(len(height))]
        left = height[0]
        right = height[-1]
        rain = 0
        
        for i in range(1, len(height)-1):
            left_max[i] = left 
            left = max(left, height[i])
        
        for i in range(len(height) - 2, 0, -1):
            right_max[i] = right 
            right = max(right, height[i])
                
        
        for i in range(1, len(height) - 1):
            temp = min(left_max[i], right_max[i])
            rain += max(0,temp - height[i])
        print(right_max, left_max)
        return rain 
                
                
            
        
########################################################
        
    def trap1(self, height: List[int]) -> int: # TLE, need to use double pointer
        max_height = max(height)
        rain = 0
        
        
        
        for i in range(max_height):
            cur_level = [0 for i in range(len(height))]
            
            for j in range(len(height)): # building current level array
                if height[j] != 0:
                    cur_level[j] += 1
                    height[j] -= 1
                    
            start =  None
            for j in range(len(height)):
                
                # first look for the place to start
                if start == None: 
                    if cur_level[j] == 0:
                        continue 
                    elif cur_level[j] == 1:
                        start = j 
                        
                
                # then look for the place to end        
                else: 
                    if cur_level[j] == 0:
                        continue
                    else:
                        amount = j - start - 1
                        
                        if amount == 0: # consecutive blocks
                            start = j
                        
                        else:
                            rain += amount 
                            print(f"Level:{i} collected {amount}")
                            start = j # setting start back to None and look for a new start.
        return rain 
                        
        
if __name__ == "__main__":
    s = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(s.trap(height))