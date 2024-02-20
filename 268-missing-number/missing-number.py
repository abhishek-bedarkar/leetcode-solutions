class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 1. Without sorting 
        # total = sum([ i for i in range(len(nums)+1)])
        # for num in nums:
        #     total -= num
        # return total

        # 2. Sorting approach
        # l = len(nums)
        # nums.sort()

        # if nums[0] != 0: return 0
        # if nums[-1] != l: return l
        # for i in range(l-1):
        #     if nums[i+1] - nums[i] != 1:
        #         return nums[i]+1

        # 3. Series formula 
        n = len(nums)
        total = n*(n +1)//2
        actual_sum = sum(nums)
        return total - actual_sum

        