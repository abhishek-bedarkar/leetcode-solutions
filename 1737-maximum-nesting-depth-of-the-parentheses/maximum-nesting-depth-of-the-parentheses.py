class Solution:
    def maxDepth(self, s: str) -> int:
        max_result, result = 0,0
        for ch in s:
            if ch == '(':
                result += 1
            if ch == ')':
                result -= 1
            
            max_result = max(max_result, result)

        return max_result
            


        