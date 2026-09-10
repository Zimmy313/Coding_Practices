from functools import cache

class Solution:
    def numDecodingsSlow(self, s: str) -> int:
        res = 0
        n = len(s)
        
        def dfs(char, i):
            nonlocal res

            if i == n - 1:
                if 1 <= int(char) <= 26:
                    res += 1
                    
            elif len(char) == 1:
                if 1 <= int(char) <= 9:
                    dfs(s[i+1], i+1)
                    dfs(s[i:i+2], i+1)
            else:
                if 10 <= int(char) <= 26:
                    dfs(s[i+1], i+1)

        dfs(s[0], 0)
        return res
    
    def numDecodings(self, s: str) -> int:

        @cache
        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            
            ways = dfs(i+1)
            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                ways += dfs(i+2)
            return ways

        return dfs(0)