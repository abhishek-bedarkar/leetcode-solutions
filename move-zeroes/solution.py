class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)

        if l > 1:
            while nums.count(0):
                nums.remove(0)
               
            nl = len(nums)
            
            for i in range(l-nl):
                nums.append(0)
        