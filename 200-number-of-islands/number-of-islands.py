class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 2

        def flood(i,j, val):
            
            grid[i][j] = val

            # down
            if 0<= i+1 < len(grid) and 0<= j < len(grid[0]):
                if grid[i+1][j] == "1":
                    grid[i+1][j] = val
                    flood(i+1,j, val)
                    
            # up
            if 0<= i-1 < len(grid) and 0<= j < len(grid[0]):
                if grid[i-1][j] == "1":
                    grid[i-1][j] = val
                    flood(i-1,j, val)
            # left
            if 0<= i < len(grid) and 0<= j-1 < len(grid[0]):
                if grid[i][j-1] == "1":
                    grid[i][j-1] = val
                    flood(i,j-1, val)
            # right
            if 0<= i < len(grid) and 0<= j+1 < len(grid[0]):
                if grid[i][j+1] == "1":
                    grid[i][j+1] = val
                    flood(i,j+1, val)
        result = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    flood(r,c, count)
                    count += 1
                if int(grid[r][c]) > result:
                    result = grid[r][c]

        return result-1 if result else 0

        
