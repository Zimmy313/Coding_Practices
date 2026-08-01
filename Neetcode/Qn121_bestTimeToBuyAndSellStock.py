class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result, l  = 0, 0
        n = len(prices)
        
        # wrong idea, you can only buy once and sell once
        # while l < n-1:
        #     buy = prices[l]
        #     sell = prices[l+1]
            
        #     if buy < sell:
        #         result += sell - buy 
        #     l += 1
        
        # kinda slow, there is a faster way
        # while l < n - 1:
        #     r = l + 1
            
        #     while r < n and prices[l] < prices[r]:
        #         profit = prices[r] - prices[l]
        #         result = max(profit, result)
        #         r += 1
            
        #     l = r
        
        lowest = prices[0]
        result = 0
        
        for price in prices:
            lowest = min(lowest, price)
            result = max(result, price - lowest)
 
        return result 
            
            
if __name__ == "__main__":
    solver = Solution()
    prices = list(map(int, input().split(",")))
    print(solver.maxProfit(prices))
        