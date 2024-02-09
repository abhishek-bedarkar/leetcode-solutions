import math
class Solution:
    memo = None
    def numSquares(self, n: int) -> int:
        t = math.floor(math.sqrt(n))
        self.memo = [[-1 for j in range(t+1)] for i in range(n+1)]

        # Top down approach
        # for i in range(n+1):
        #     for j in range(t+1):
        #         if n ==0 or n==1 or t==1:
        #             self.memo[n][t] = n
        #         elif t**2<= n:
        #             self.memo[n][t] = min(1+self.memo[n-t**2][t], self.memo[n][t-1])
        #         else:
        #             self.memo[n][t] = self.memo[n][t-1]
 
        return self.ps(n, t)
        

    def ps(self, n:int, t:int)-> int:
        # Base condition   
        if n ==0 or n==1 or t==1:
            self.memo[n][t] = n
            return n
        if self.memo[n][t] == -1:
            if t**2<= n:
                self.memo[n][t] = min(1+self.ps(n-t**2, t), self.ps(n, t-1))
                return self.memo[n][t]
            else:
                self.memo[n][t] = self.ps(n, t-1)
                return self.memo[n][t]
        else:
            return self.memo[n][t]