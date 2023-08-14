class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s_r = 0
        s_l = 0
        size = len(nums)
        sum_left = [None]*size
        sum_right = [None]*size
        for i in range(size):
            sum_right[size-1-i] = s_r
            sum_left[i] = s_l
            
            s_l += nums[i]
            s_r += nums[size-1-i]

        # print(sum_left)
        # print(sum_right)
        for i in range(size):
            if sum_left[i] == sum_right[i]:
                return i
        
        return -1