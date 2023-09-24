class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = len(s)
        if l==1 or l==0:
            return l

        max_length = 1
        i=0
        while(i < l-1):
            length = 1
            j=i+1
            
            if j<=l:
                while s[j] not in s[i:j]:
                    length += 1
                    j += 1
                    if j>=l:
                        break

            if length>max_length:
                max_length = length
            i += 1

        return max_length