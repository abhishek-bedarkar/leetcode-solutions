class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        result,l = 0, len(grid)
        # Iterate row
        for i in range(l) :

            # create column
            c = [grid[j][i] for j in range(l)]

            # if column in rows, add count of columns found to result
            if c in grid:
                result += grid.count(c)

        return result

        