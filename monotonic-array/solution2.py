class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        l = len(nums)
        if l == 1: return True
        i=0
        while i < l-2:
            j = i+1
            
            if nums[i] == nums[j]:
                i +=1
            else:
                break
        
        if i == l-2:
            return True
        else:
            if nums[i]<nums[j]:
                # check for monotonically increasing 
                while i < l-2:
                    i += 1
                    j += 1
                    if nums[i]>nums[j]:
                        return False
                    
            else:
                # check of monotonically decreasing
                while i < l-2:
                    i +=1 
                    j +=1
                    if nums[i]<nums[j]:
                        return False
                    
            return True