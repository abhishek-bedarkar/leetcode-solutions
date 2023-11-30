class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_vol = 0
        left=0 
        right = len(height)-1

        while left < right:
            current_vol = (right-left) * min(height[left],height[right])
            max_vol = max(current_vol, max_vol)

            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1

        return max_vol