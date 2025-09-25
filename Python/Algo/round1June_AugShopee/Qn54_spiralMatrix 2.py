from typing import *

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        res = []
        while left < right and top < bottom:
            for i in range(left, right):    
                res.append(matrix[top][i]) 
            top+=1

            for i in range(top, bottom): # no need to check as if top > bottom, it wont be excuted. no overstep
                res.append(matrix[i][right - 1])
            right-=1

            if not(left  < right and top < bottom): # need this to avoid duplicates and mis-steps. try matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] by removing it
                break
            
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom-=1

            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left+=1
        return res
    
    def spiralOrder2(self, matrix: List[List[int]]) -> List[int]: # dont really need to keep track of moves. Check every 2 motion.
        top, bottom = 0, len(matrix)-1
        left, right = 0, len(matrix[0])-1
        
        moves  = ["Forward", "Downward", "Backward", "Upward"]
        counter = 0
        result = []
        
        while top <= bottom and left <= right:
            index  = counter % 4
            move = moves[index]
            
            if move == "Forward":
                
                for i in range(left, right+1):
                    result.append(matrix[top][i])
                top += 1
                counter += 1
            
            elif move == "Downward":
                
                for i in range(top, bottom+1):
                    result.append(matrix[i][right])
                    
                right -= 1
                counter += 1
                
            elif move == "Backward":
                
                for i in range(right, left - 1 , -1):
                    result.append(matrix[bottom][i])
                   
                bottom -= 1
                counter += 1
            else:
                for i in range(bottom, top - 1 , -1):
                    result.append(matrix[i][left])
                   
                left += 1
                counter += 1
        return result 
                
                
        
        
        
    
    def spiralOrder1(self, matrix: List[List[int]]) -> List[int]: # false attemp. overly complicated and did not keep track of all 4 boundaries. Should not use offset in 
        # range(limits - 1) and should not first append matrix[0][0] to result. As a result, breaks down after first spiral.
        
        horizontal = True # move horizontal if true
        
        vLimit = len(matrix)
        hLimit = len(matrix[0])
        result = [matrix[0][0]]
        total = hLimit*vLimit
        
        hReverse = False
        vReverse = False
        x, y = 0, 0 # starting point
        
        while len(result) != total:
            if horizontal == True:
                if hReverse == False: # going forward
                    print("Going forward!")
                    for i in range(hLimit-1):
                        x += 1
                        
                        print((y,x))
                        current = matrix[y][x]
                        result.append(current)
                    hReverse = True
                    horizontal = False
                        
                else: # going backward
                    print("Going backward!")
                    for i in range(hLimit-1):
                        x -= 1
                        
                        print((y,x))
                        current = matrix[y][x]
                        result.append(current)
                    hReverse = False
                    hLimit -= 1
                    horizontal = False
            else:
                if vReverse == False: # going downwards
                    print("Going downward!")
                    for i in range(vLimit-1):
                        y += 1
                        
                        print((y,x))
                        current = matrix[y][x]
                        result.append(current)
                    vReverse = True  
                    horizontal = True
                    vLimit -= 1
                
                else:
                    print("Going upward!")
                    for i in range(vLimit -1):
                        y -= 1
                        
                        print((y,x))
                        current = matrix[y][x]
                        result.append(current)
                    vReverse = False
                    horizontal = True
        return result
    
if __name__ == "__main__":
    s = Solution()
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20],[21,22,23,24]]
    print(s.spiralOrder(matrix))
                        
        