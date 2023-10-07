class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        
        dp = [[0] * (k+1) for _ in range(m+1)]
        prefix = [[0] * (k+1) for _ in range(m+1)]
        prev_dp = [[0] * (k+1) for _ in range(m+1)]
        prev_prefix = [[0] * (k+1) for _ in range(m+1)]
        
        for j in range(1, m+1):
            prev_dp[j][1] = 1
            prev_prefix[j][1] = j
        
        for _ in range(2, n+1):
            dp = [[0] * (k+1) for _ in range(m+1)]
            prefix = [[0] * (k+1) for _ in range(m+1)]
            
            for max_num in range(1, m+1):
                for cost in range(1, k+1):
                    dp[max_num][cost] = (max_num * prev_dp[max_num][cost]) % MOD
                    
                    if max_num > 1 and cost > 1:
                        dp[max_num][cost] += prev_prefix[max_num - 1][cost - 1]
                        dp[max_num][cost] %= MOD
                    
                    prefix[max_num][cost] = (prefix[max_num - 1][cost] + dp[max_num][cost]) % MOD
            
            prev_dp, prev_prefix = [row[:] for row in dp], [row[:] for row in prefix]
        
        return prefix[m][k]
