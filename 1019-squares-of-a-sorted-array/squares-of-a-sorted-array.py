class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = sorted([num**2 for num in nums])
        return result
        