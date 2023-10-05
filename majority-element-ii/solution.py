from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        n = len(nums)//3
        count_dict = Counter(nums)      
        return [ k for k,v in count_dict.items() if v>n]
        