class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Initialize right left to zero
        l,r =0,0

        # Iterate right for elements in nums    
        for r in range(len(nums)):
            
            # When found zero
            if nums[r] == 0:
                k -=1 
            
            # Increment window when no more zeros allowed
            if k< 0:
                if nums[l] == 0:
                    k += 1
                l += 1
            
        return r-l + 1



        