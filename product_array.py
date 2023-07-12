class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        result = [0]*len(nums)
        
        if 0 in nums:
            zero_count = 0
            for i in nums:
                if i != 0:
                    product *= i
                else:
                    zero_count += 1

            for i in range(len(nums)):
                if nums[i] != 0:
                    result[i] = 0
                else:
                    if zero_count == 1 :
                        result[i] = product
                    else:
                        result[i] = 0
        else:
             
            for i in nums:
                product *= i
            for i in range(len(nums)):
                result[i]= product//nums[i]
        
        return result
