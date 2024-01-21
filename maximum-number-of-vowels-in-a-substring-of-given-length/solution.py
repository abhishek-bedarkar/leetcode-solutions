class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        conv=""
        vowels = ['a','e','i','o','u']

        for c in s:
            if c in vowels:
                conv += '1'
            else:
                conv += '0'
        count = 0
        
        for i in range(len(conv)-k+1):
            count = max(count, str(conv[i:i+k]).count('1'))

            if count == k:
                break
        return count