class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count=0
        if len(nums)==0:
            return 0
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                nums[i-1]=-99999
                count += 1
                
        nums.sort()
        
        while count != 0 :
            nums.pop(0)
            count -= 1
            
        
        return len(nums)