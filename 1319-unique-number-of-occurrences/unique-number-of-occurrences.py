from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num_dict = Counter(arr)
        values_uniq = set(num_dict.values())

        for k,v in num_dict.items():
            if v in values_uniq:
                values_uniq.remove(v)
            else:
                return False
        return True
        