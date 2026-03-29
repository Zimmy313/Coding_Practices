from collections import deque

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        left = []
        left_rolling = 0

        right = deque([])
        right_rolling = 0
        right_index = n-1

        for i in range(n):
            left.append(left_rolling)
            left_rolling += nums[i]

            right.appendleft(right_rolling)
            right_rolling += nums[right_index]
            right_index -= 1
        

        for i in range(n):
            if left[i] == right[i]:
                return i
            
        return -1

