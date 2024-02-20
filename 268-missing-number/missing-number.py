class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = sum([ i for i in range(len(nums)+1)])
        for num in nums:
            total -= num
        return total
        