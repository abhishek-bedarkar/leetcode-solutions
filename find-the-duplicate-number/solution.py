class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        unique = set()

        for i in range(len(nums)):
            unique.add(nums[i])

            if len(unique)!= i+1:
                return nums[i]