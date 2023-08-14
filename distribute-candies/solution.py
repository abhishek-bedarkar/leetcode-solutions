class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        s=set(candyType)
        unique_candies = len(s)
        doctor_allowed = int(len(candyType)/2)
        if unique_candies>= doctor_allowed:
            return doctor_allowed
        else:
            return unique_candies