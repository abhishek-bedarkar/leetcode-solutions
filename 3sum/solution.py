class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[k] == 0:
                        temp_result = sorted([nums[i],nums[j],nums[k]])
                        if temp_result not in result:
                            result.append(temp_result)
        
        return result


s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))