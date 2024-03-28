class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counter = {}
        left, right = 0, 0
        max_length = 1
        while right< len(nums):
            if nums[right] not in counter.keys():
                counter[nums[right]] = 1
            else:
                counter[nums[right]] += 1
            
            if counter[nums[right]]<= k:
                # so far good
                max_length = max(max_length, 1 + right-left)   
            else:
                # not good
                while counter[nums[right]]>k:
                    counter[nums[left]] -= 1 
                    left += 1

            right += 1
        return max_length