class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # brute force
        # profit  = 0

        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         profit = max(profit, prices[j] - prices[i])

        # return profit
        # O(1) / O(n*2)

        # two pointer
        if len(prices) <2: return 0

        left,right,profit = 0,1,0

        while right < len(prices):
            if prices[left] >= prices[right]:
                left = right
                right = left + 1
            else:
                profit = max(profit, prices[right] - prices[left])
                right += 1
        # O(N)
        return profit


        





        




        