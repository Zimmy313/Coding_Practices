class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r = len(nums) - 1
        l = 0

        while l<r:
            m = l + (r-l) // 2

            if nums[m] > nums[r]: # left is sorted
                if target <= nums[m] and target >= nums[l]: # in the sorted part
                    r = m
                else:
                    l = m + 1
            else: # right is sorted
                if target > nums[m] and target <= nums[r]: # in the sorted part
                    l = m + 1
                else:
                    r = m
        
        return l if nums[l] == target else -1
                