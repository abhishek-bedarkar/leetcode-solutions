class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s)==0:
            return 0
        else:
            length=0
            for w in s.split(' '):
                if w != '' :
                    length=len(w)
            return length