class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        left, right, diff, max_len = 0, 0, 0, 0
        # [1, 1, 1, 2]
        
        while left < len(s) and right< len(t):
            curr_ele_diff = abs(ord(s[right]) - ord(t[right]))
            if curr_ele_diff > maxCost:
                left = right + 1
                right = left
                diff = 0
            else:
                # expand window
                if diff + curr_ele_diff <= maxCost:
                    diff += curr_ele_diff
                    right += 1
                    max_len = max(max_len, right - left)
                    #print(f' left {left}, right {right}, max_len {max_len}')
                # Shrink window
                else:
                    diff -= abs(ord(s[left]) - ord(t[left]))
                    left += 1
        
        return max_len


