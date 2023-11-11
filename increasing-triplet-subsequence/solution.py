class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        if len(nums)<2:
            return False

        f_min = float("inf")
        s_min = float("inf")

        for num in nums:

            if num <= f_min:
                f_min = num
            elif num <= s_min:
                s_min = num
            else:
                return True

        return False