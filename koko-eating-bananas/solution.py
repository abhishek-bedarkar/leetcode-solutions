class Solution:

    def eating_hours(self, piles, rate, h)->int:
        total_hour = 0
        for p in piles:
           total_hour += math.ceil(p / rate)
           if total_hour > h:
               break
        return total_hour
                


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        mid  = low + (high-low)//2

        result = high

        while low <= high:
            if self.eating_hours(piles, mid, h) <= h:
                if mid < result:
                    result = mid
                high = mid - 1
            else:
                low = mid + 1

            mid  = low + (high-low)//2

        return result