class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        if n == 0 :
            return [-1,-1]
        
        h = n-1
        l = 0
        m = l + (h-l)//2
              
        while (l < h):
            if nums[m] == target:
                break
            elif nums[m]>target:
                h = m
            else:
                l = m+1
            
            m = l +(h-l)//2
        
        if nums[m] != target:
            return [-1,-1]

        first = m
        last = m
        while first-1 >= 0 and nums[first-1] ==  target:
            first -=1
        
        while last +1  < n and nums[last+1] ==  target :
            last += 1
        
        return [first, last]