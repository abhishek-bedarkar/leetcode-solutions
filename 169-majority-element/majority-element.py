from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict = Counter(nums)
        maj = len(nums)//2 + 1
        for k,v in count_dict.items():
            if v >= maj:
                return k



        