class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        # sub_length, min_length = len(t), len(t)
        # left, right = 0, 0

        # while left < len(s):
        #     if right == len(t):
        #         return 0

        #     if s[left] == t[right]:
        #         sub_length -= 1
        #         left += 1
        #         right += 1
        #     else:
        #         if right == 0:
        #             left += 1
        #         else:
        #             min_length = min(min_length, sub_length)
        #             sub_length = len(t)
        #             right = 0
        # min_length = min(min_length, sub_length)
        # return min_length

        # Initialize pointer for t
        j = 0
        # Traverse through s
        for char in s:
            # If the current character in s matches the current character in t
            if j < len(t) and char == t[j]:
                # Move to the next character in t
                j += 1
        return len(t) - j

