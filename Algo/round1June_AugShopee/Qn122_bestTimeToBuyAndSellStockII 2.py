from typing import *

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        share = False
        for i in range(len(prices)-1):
            if share: # sell if holding
                res += prices[i]
                share = False
                
            dif = prices[i+1] - prices[i]
            
            if dif > 0:
                res -= prices[i] # buy in 
                share = True
        if share:
            res += prices[-1]
        
        if res < 0:
            return 0 
        
        return res

if __name__ == "__main__":
    s = Solution()
    prices = [1,2,3,4,5]
    print(s.maxProfit(prices ))
                
            
            
        