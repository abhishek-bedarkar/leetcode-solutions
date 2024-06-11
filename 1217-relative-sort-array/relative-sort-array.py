from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result, cnt = [], Counter(arr1)

        # for elm in arr2:
        #     for i in range(cnt[elm]):
        #         result.append(elm)

        result = [elm for elm in arr2 for i in range(cnt[elm])]
        for elm in sorted(set(arr1) - set(arr2)):
            for i in range(cnt[elm]):
                result.append(elm)
        return result
