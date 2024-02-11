class Solution:
    def countSubstrings(self, s: str) -> int:
        # Brute force 
        # result = 0
        # for i in range(len(s)):
        #     for j in range(i,len(s)):
        #         sr=s[i:j+1]
        #         if s[i:j+1] == sr[::-1]:
        #             result += 1
        # return result

        # Odd even strategy
        n, result = len(s), 0
        
        def palindromeCount(left: int, right: int) -> int:
            count = 0

            # Palindrom condition
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            return count
        
        for i in range(n):
            # Even cases
            even = palindromeCount(i, i + 1)

            # Odd cases
            odd = palindromeCount(i, i)
            result += even + odd
            
        return result



                
                    



        