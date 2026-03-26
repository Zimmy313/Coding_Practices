from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        bed_length = len(flowerbed)
        ptr = 0
        
        if n == 0:
            return True

        # edge case
        if bed_length == 1: 
            if flowerbed[0] == 0 and n <= 1:
                return True
            else:
                return False

        while ptr < bed_length:
            if ptr == 0:
                if flowerbed[ptr] == 0 and flowerbed[ptr+1] == 0:
                    flowerbed[ptr] = 1
                    n -= 1
                    
            elif ptr == bed_length - 1:
                if flowerbed[ptr] == 0 and flowerbed[ptr-1] == 0:
                    flowerbed[ptr] = 1
                    n -= 1

            else:
                if flowerbed[ptr] == 0 and flowerbed[ptr-1] == 0 and flowerbed[ptr+1] == 0:
                    flowerbed[ptr] = 1
                    n -= 1
            
            ptr += 1
        
        return n <= 0
    
                

if __name__ == "__main__":
    print("Please enter flowerbed")
    flowerbed = list(map(int, input().split(",")))
    
    print("Please enter n")
    n = int(input())
    
    s = Solution()
    print(s.canPlaceFlowers(flowerbed, n))
    
    
    