from collections import Counter
from collections import defaultdict
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        ## Counter approach
        # num_dict = Counter(arr)
        # sorted_num_dict = {k:v for k,v in sorted(num_dict.items(), key = lambda x: x[1], reverse = False)}
        # key_list = list(sorted_num_dict.keys())
        # key = key_list[0]
        # for i in range(k):
        #     val = sorted_num_dict[key]
        #     if val == 1:
        #         key_list.remove(key)
        #         del sorted_num_dict[key]
        #         if len(key_list):
        #             key = key_list[0]
        #     else:
        #         sorted_num_dict[key] -= 1
        # return len(sorted_num_dict.keys())

        ## List appraoch
        num_dict = Counter(arr)
        sorted_val = sorted(num_dict.values())
        freq = len(num_dict.keys())

        for v in sorted_val:
            if k >= v:
                k -= v
                freq -= 1
            else:
                break

        return freq



