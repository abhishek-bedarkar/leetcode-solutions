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
            high = len(sorted_nums)-1
            while(low != high):
                if target_sum == sorted_nums[low] + sorted_nums[high]:
                    temp_sol = [sorted_nums[i],sorted_nums[low],sorted_nums[high]]
                    if temp_sol not in result:
                        result.append(temp_sol)
                    low += 1
                elif target_sum > sorted_nums[low] + sorted_nums[high]:
                    low += 1
                else:
                    high -= 1
        return result
                    

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))