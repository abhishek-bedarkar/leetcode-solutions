from unittest import result


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sorted_nums = sorted(nums)
        result = []
        for i in range(len(sorted_nums)-1):
            if sorted_nums[i]>0:
                break
            target_sum = - sorted_nums[i]
            low = i+1
            high = len(sorted_nums)
            while(low != high):
                if target_sum == sorted_nums[low] + sorted_nums[high]:
                    pass