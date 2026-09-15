class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        
        def dfs(amount: int) -> int:
            if amount == 0:
                return 0
            
            if amount in memo:
                return memo[amount]
            
            if amount < 0 :
                return -1
            
            minimum = float("inf")

            for coin in coins:
                temp = dfs(amount - coin)
                if temp == -1:
                    continue
                
                minimum = min(minimum, temp + 1)
            
            memo[amount] = -1 if minimum == float("inf") else minimum
            return memo[amount]
        
        return dfs(amount)
                