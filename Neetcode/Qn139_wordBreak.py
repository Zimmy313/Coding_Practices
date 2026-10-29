class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dfs(i) -> bool:
            if i == len(s):
                return True
            
            for word in wordDict:
                n = len(word)

                if i+n <= len(s) and s[i:i+n] == word:
                    if i+n not in memo:
                        memo[i+n] = dfs(i+n)
                    
                    if memo[i+n]:
                        return memo[i+n]
            
            return False
        
        return dfs(0)


                