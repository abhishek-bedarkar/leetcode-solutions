class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        elif needle == haystack:
            return 0
        else:
            return haystack.find(needle)