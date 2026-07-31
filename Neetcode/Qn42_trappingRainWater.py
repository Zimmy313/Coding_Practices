from collections import deque

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        result = 0
        
        while left != right:
            if heights[left] < heights[right]:
                height = heights[left]
                width = right - left
                left += 1
            else:
                height = heights[right]
                width = right - left
                right -= 1
            
            
            temp = height * width
            
            if temp > result:
                result = temp 
            
        return result 
    
    def trap(self, height: List[int]) -> int:
        result = 0
        
        # # not the optimal way to build
        # prefix = [0]
        # postfix = deque([0])
        # temp = 0        
        # for i in range(1, len(height)):
        #     temp = max(temp, height[i-1])
        #     prefix.append(temp)
        
        # temp = 0
        
        # for i in range(len(height) - 2, -1, -1):
        #     temp = max(temp, height[i+1])
        #     postfix.appendleft(temp)
        
        n = len(height)
        prefix = [0] * n
        postfix = [0] * n
        
        for i in range(1, n):
            prefix[i] = max(prefix[i-1], height[i-1])
        for i in range(n-2, -1, -1):
            postfix[i] = max(postfix[i+1], height[i+1])
        
        for i in range(0, len(height)):
            left, right, middle = prefix[i], postfix[i], height[i]
            
            if left == 0 or right == 0 or middle > left or middle > right:
                continue
            
            current = min(left, right) - middle
            result += current
        
        return result
        
        
        
    

if __name__ == "__main__":
    solver = Solution()
    # heights = list(map(int, input().split(",")))
    # print(solver.maxArea(heights))
    
    height = list(map(int, input().split(",")))
    print(solver.trap(height))
    
    
            
            
            
            
            