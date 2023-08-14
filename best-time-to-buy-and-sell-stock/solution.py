class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low=999999
        high=0
        profit=0
        for i in range(0,len(prices)):
            if (prices[i] < low) : 
                low= prices[i]

            elif (prices[i]- low >profit)  :
                profit=prices[i]-low
        return profit