from typing import *

class Solution:
    def maxProfit1(self, prices: List[int]) -> int: # double for loop. TLE
        
        n = len(prices)
        result = -float("inf")
        for i in range(n):
            
            for j in range(i,n):
                dif = prices[j] - prices[i]
                if dif > result:
                    result = dif 
        
        if result < 0:
            return 0
        
        return result
    
    def maxProfit(self, prices: List[int]) -> int:
        start = prices[0]
        maximum = -float("inf")
        
        for i in range(1, len(prices)):
            dif = prices[i] - start 
            maximum = max(maximum, dif)
            start = min(start, prices[i])
        
        if maximum < 0:
            return 0
        return maximum
            
        
        
    
if __name__ == "__main__":
    s = Solution()
    prices = [7,1,5,3,6,4]
    print(s.maxProfit(prices=prices))