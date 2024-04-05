class Solution:
    def makeGood(self, s: str) -> str:
        result = []
        for c in s:
            if len(result) == 0:
                result.append(c)
            else:
                if (result[-1] != c) and (result[-1].upper() == c or result[-1] == c.upper()):
                    result.pop()
                else:
                    result.append(c)

        return ''.join(result)
                    
        