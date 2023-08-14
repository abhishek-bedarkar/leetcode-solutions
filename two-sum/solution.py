class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            select = nums[i]
            findNum = target - select
            if findNum in nums[i+1:]:
                ind = nums[i+1:].index(findNum)
                return [i,ind+i+1]