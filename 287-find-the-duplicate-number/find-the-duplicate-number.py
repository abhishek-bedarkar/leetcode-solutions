class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        id = set()

        for num in nums:
            if num not in id:
                id.add(num)
            else:
                return num