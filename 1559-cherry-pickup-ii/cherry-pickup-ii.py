class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        moves = [-1,0,1]
        n = len(grid[0])
        m = len(grid)

        @lru_cache(None)
        def dp(i,j,k):
            
            if i>=m: return 0

            if not  0<= j <= k <n : return -inf

            # if j==k:
            #     ans = grid[i][j]
            # else:
            #     ans = grid[i][j] + grid[i][k]  

            ans = grid[i][j] + (j != k)* grid[i][k]
            return ans + max(dp(i+1, j+x, k+y) for x in moves for y in moves)
            
        return dp(0,0,n-1)