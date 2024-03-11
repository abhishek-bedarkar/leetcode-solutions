class Solution:
    def customSortString(self, order: str, s: str) -> str:
        result = ""
        for c in order:
            if c in s:
                cnt = s.count(c)
                s = s.replace(c,'',cnt)
                result += c*cnt
        result += s
        return result

        