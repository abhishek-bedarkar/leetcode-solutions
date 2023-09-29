class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        d_count = 1
        i_count = 1
        for i in range(0,len(nums)-1):
            # Decreasing
            j = i+1
            if nums[i] >= nums[j] :
                d_count += 1
            # Increasing
            if  nums[i] <= nums[j] :
                i_count += 1

        if d_count == len(nums) or i_count == len(nums):
            return True
        else:
            return False