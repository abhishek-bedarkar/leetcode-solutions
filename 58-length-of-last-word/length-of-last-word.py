class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #return len(s.rstrip().split(' ')[-1])
        last = len(s)-1
        while last > 0 and s[last] == ' ' :
            last -= 1 

        result = 0

        while s[last] != ' ':
            last -= 1
            result += 1
            if last < 0:
                return result
        return result 
        