class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        size = len(nums)
        if size%2 == 1:
            n = (size+1)/2
        else:
            n = size/2
          
        if size==1 and n==1:
            return nums[0]
        nums.sort()
        count=1
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                count +=1
                if count >= n:
                    return nums[i]
                
            else :
                count=1
        
        return 1