class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum([ 1 for i, elm in enumerate(sorted(heights)) if heights[i] != elm])