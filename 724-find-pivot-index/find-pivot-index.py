class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # total sum
        total = sum(nums)
        left_sum= 0

        # Iterate array to check condition : total = 2*left + current number
        for i in range(len(nums)):
            if  total == nums[i] + left_sum*2:
                return i
            
            left_sum += nums[i]
            
        return -1
    




        

        