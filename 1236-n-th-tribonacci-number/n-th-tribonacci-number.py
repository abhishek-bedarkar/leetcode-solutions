class Solution:

    def tribonacci(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        
        if n == 2:
            return 1

        fibo = [0,1,1]
        for i in range(3, n+1):
            fibo[i%3] = sum(fibo)
        
        return fibo[n%3]

        