class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "#": 0}
        number = 0
        s = s + '#'
        i=0
        while  i != len(s)-1:
            if dic[s[i]] < dic[s[i + 1]] and (s[i] in ("I", "X", "C")):
                # case where merging needed
                number = number + (dic[s[i + 1]] - dic[s[i]])
                i += 2
            else:
                number = number + dic[s[i]]
                i += 1
        return number