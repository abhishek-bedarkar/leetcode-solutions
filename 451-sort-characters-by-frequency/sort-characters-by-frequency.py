from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        # Create a counter dictionary for s
        char_count = Counter(s)

        # Sort and create a result char list 
        sorted_char = [k*v for k,v in sorted(char_count.items(), key = lambda x: x[1], reverse=True)]
        
        # Return result string by joining chars 
        return ''.join(sorted_char)

        