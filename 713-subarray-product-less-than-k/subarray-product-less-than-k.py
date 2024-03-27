class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        # two pointer approach
        if k <= 1 : return 0

        left, right, prod, count = 0,0,1, 0

        while right < len(nums):
            prod *= nums[right]
            while prod >= k:
                prod //= nums[left]
                left += 1
            
            count += 1 + (right - left)
            #print("PROD : {}, left : {}, right : {}, count : {}".format(prod, left, right, count))
            right += 1

            

        return count 

                

