class Solution:
    def maxDepth(self, s: str) -> int:
        max_result, result = 0,0
        for ch in s:
            if ch == '(':
                result += 1

                if result > max_result:
                    max_result = result

            if ch == ')':
                result -= 1

        return max_result
            


        