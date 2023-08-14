class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max=nums[0]
        final_max=nums[0]
        
        for i in range(1,len(nums)):
            
            curr_max=max(nums[i],curr_max + nums[i])
            final_max= max(final_max,curr_max)
        return final_max
                
        
        