class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for letter in s:
            if letter in t:
                t = t.replace(letter,"",1)
            else:
                return False
        if len(t) == 0:
            return True
