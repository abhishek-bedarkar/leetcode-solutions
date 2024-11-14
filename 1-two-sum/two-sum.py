class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} 
        for i,num in enumerate(nums):
            hashmap[num] = i
        
        for i in range(len(nums)):
            find_elm = target - nums[i]
            if find_elm in hashmap and hashmap[find_elm] != i:
                return [i, hashmap[find_elm]]