class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        id = dict()

        for num in nums:
            if num not in id.keys():
                id[num] = 1
            else:
                return num