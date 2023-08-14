class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count_dict = dict()
        for i in range(0,len(nums)):
            if nums[i] in count_dict.keys():
                count_dict[nums[i]] = count_dict[nums[i]] + 1
            else:
                count_dict[nums[i]] = 1
        
        sorted_dict = {key: val for key, val in sorted(count_dict.items(), key=lambda item: item[1], reverse=True)}

        return list(sorted_dict.keys())[:k]