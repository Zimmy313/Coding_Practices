from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        result = [False]*n
        top = max(candies)

        for i in range(n):
            if candies[i] + extraCandies >= top:
                result[i] = True
            
        return result
    

if __name__ == "__main__":
    print("Enter the child list")
    candies = list(map(int, input().split()))
    
    print("Enter the extra candies")
    extraCandies = int(input())
    
    s = Solution()
    print(s.kidsWithCandies(candies, extraCandies))

