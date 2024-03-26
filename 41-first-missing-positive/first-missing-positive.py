class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        unq_nums = set()
        for num in nums:
            if num>0:
                unq_nums.add(num)
        
        for i in range(1,len(nums)+2):
            if i not in unq_nums:
                return i


        