from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        need = Counter(t)
        window = defaultdict(int)

        have = 0
        required = len(need.keys())

        result = [-1, -1]
        res_len = float("inf")

        # no need
        # if len(s) < len(t):
        #     return ""

        for r in range(len(s)):
            char = s[r]
            window[char] += 1

            if char in need and window[char] == need[char]:
                have += 1
            
            while have == required:

                # shorter substring found
                if (r - l + 1) < res_len:
                    result = [l,r]
                    res_len = r - l + 1
                
                left_char = s[l]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                
                l += 1
            
        l , r = result

        return "" if res_len == float("inf") else s[l: r+1]




            


