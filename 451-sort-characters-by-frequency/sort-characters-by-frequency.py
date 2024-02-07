from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        char_count = Counter(s)
        sorted_char_count = {k:v for k,v in sorted(char_count.items(), key = lambda x: x[1], reverse=True)}
        result = ""
        for k,v in sorted_char_count.items():
            result += k*v

        return result

        