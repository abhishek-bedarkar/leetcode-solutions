class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x
        mid = start + (end - start) // 2
        ans = 0

        if x == 1:
            return 1
        while start < end:
            sq = mid * mid

            if sq == x:
                return mid
            elif sq > x:
                end = mid
            else:
                ans = mid
                start = mid + 1
            mid = start + (end - start) // 2
        return ans