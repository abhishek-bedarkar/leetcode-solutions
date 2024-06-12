class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        color = {0:0, 1:0, 2:0}

        for num in nums:
            color[num] += 1
        
        i = 0
        while i < len(nums):
            if color[0] > 0:
                nums[i] = 0
                color[0] -= 1
            elif color[1] > 0:
                nums[i]= 1
                color[1] -= 1
            elif color[2] > 0:
                nums[i]= 2
                color[2] -= 1
            
            i += 1
        