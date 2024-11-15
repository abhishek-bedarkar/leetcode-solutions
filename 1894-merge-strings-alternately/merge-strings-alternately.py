class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        left, right, result = 0, 0,  ""

        while left < len(word1) and right < len(word2):
            result += word1[left]
            left += 1

            result += word2[right]
            right +=1 
        
        if left < len(word1):
            result += word1[left:]
        elif right < len(word2):
            result += word2[right:]

        return result
