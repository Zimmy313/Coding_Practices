class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        n = len(s)
        result = 0
        seen = set()
        
        # Wrong
        # while l < n -1:
        #     map = set()
        #     map.add(s[l])
            
        #     r = l + 1
            
        #     while r < n:
        #         char = s[r]
                
        #         if char in map:
        #             score = r - l
        #             result = max(score, result)
                    
        #             l = r
        #             break
                    
        #         else:
        #             map.add(char)
        #             r += 1
        
        # classical sliding window approch
        for r in range(n):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            result = max(result, r - l + 1)            
            
        
        return result 
    

if __name__ == "__main__":
    solver = Solution()
    s = input()
    
    print(solver.lengthOfLongestSubstring(s = s))
            
            