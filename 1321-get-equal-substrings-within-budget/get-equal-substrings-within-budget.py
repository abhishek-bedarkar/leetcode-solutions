class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        diff_arr = []

        for i in range(len(s)):
            diff_arr.append(abs(ord(s[i]) - ord(t[i])))
        
        #print(diff_arr)

        left, right, diff, max_len = 0, 0, 0, 0
        # [1, 1, 1, 2]
        
        while left < len(diff_arr) and right< len(diff_arr):

            if diff_arr[right] > maxCost:
                left = right + 1
                right = left
                diff = 0
            else:
                # expand window
                if diff + diff_arr[right] <= maxCost:
                    diff += diff_arr[right]
                    right += 1
                    max_len = max(max_len, right - left)
                    #print(f' left {left}, right {right}, max_len {max_len}')
                # Shrink window
                else:
                    diff -= diff_arr[left]
                    left += 1
        
        return max_len




