class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        max_freq = 0
        res = 0
        l = 0

        for r in range(len(s)):

            freq[s[r]] = freq.get(s[r], 0) + 1

            # char with most repetition
            max_freq = max(max_freq, freq[s[r]])

            # more than k edits
            # need not update max_freq here as it records historical best.
            if r-l+1 - max_freq > k:
                freq[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res

            
