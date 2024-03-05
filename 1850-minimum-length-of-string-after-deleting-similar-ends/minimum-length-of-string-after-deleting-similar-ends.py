class Solution:
    def minimumLength(self, s: str) -> int:
        l = len(s)
        left = 0
        right = l-1
        if l == 1:
            return 1
        while left < right:
            if s[left] != s[right]:
                break
            else:
                while left+1<right and s[left] == s[left+1] :
                    left += 1
                while right -1 > left+1 and s[right] == s[right-1] :
                    right -= 1
                left += 1
                right -= 1

        return len(s[left:right+1])
        