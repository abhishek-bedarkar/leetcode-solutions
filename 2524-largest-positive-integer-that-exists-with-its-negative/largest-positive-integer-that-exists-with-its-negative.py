class Solution:
    def findMaxK(self, nums: List[int]) -> int:
       nums.sort()
       left, right = 0, len(nums)-1
       #print(nums)

       max_found = 0
       while left < right:
            #print(f'check {nums[left]} -> {nums[right]}')
            if nums[left] + nums[right] == 0:
                return abs(nums[left])
            elif abs(nums[left]) < abs(nums[right]):
                right -= 1
            else:
                left += 1

       return -1


# -7 -1 1 6 7 10
# -10 -3 -2 6 7 8