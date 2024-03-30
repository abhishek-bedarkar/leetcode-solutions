class Solution:
    def slidingWindow(self, nums: List[int], k: int) -> int:
        length,left, right, result, ctr = len(nums), 0, 0, 0,{}

        while right < length:
            ctr[nums[right]] = ctr.get(nums[right], 0) + 1
            
            while len(ctr) > k:
                ctr[nums[left]] -= 1
		
                if ctr[nums[left]] == 0:
                    del ctr[nums[left]]
                left += 1
            
            result += right - left + 1
			
            right += 1
        
        return result
    
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.slidingWindow(nums, k) - self.slidingWindow(nums, k - 1)