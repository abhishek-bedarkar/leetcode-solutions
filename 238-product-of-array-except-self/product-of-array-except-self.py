class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        all_product = 1
        zero_count =0
        for num in nums:
            if num != 0:
                all_product *= num
            else:
                zero_count += 1
            if zero_count >=2:
                break
        
        if zero_count >=2:
            return [0]*len(nums)
        
        result = []
        for num in nums:
            if num != 0:
                if zero_count==0:
                    result.append(all_product//num)
                else:
                    result.append(0)
            else:
                if zero_count == 1:
                    result.append(all_product)
                else:
                    result.append(0)

        return result
        