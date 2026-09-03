class Solution:
    def climbStairs(self, n: int) -> int:
        seen = {}

        def helper(m):
            if m in seen:
                return seen[m]
            elif m == 1:
                seen[1] = 1
                return 1
            elif m == 2:
                seen[2] = 2
                return 2

            seen[m] = helper(m-1) + helper(m-2)
            return seen[m]

        return helper(n)       
