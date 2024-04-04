class Solution:
    def maxDepth(self, s: str) -> int:
        stack, result = [], 0
        for ch in s:
            if ch == '(':
                stack.append('(')
            if ch == ')':
                stack.pop()
            
            result = max(result, len(stack))

        return result
            


        