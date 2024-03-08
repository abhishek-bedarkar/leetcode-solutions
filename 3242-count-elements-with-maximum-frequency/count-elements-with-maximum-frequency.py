from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        ctr = Counter(nums)        
        max_val, result  = max(ctr.values()), 0
        
        for k,v in ctr.items():
            if v == max_val:
                result += max_val
        return result