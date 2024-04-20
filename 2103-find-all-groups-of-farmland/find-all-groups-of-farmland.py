class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        row, col, count = len(land),len(land[0]),  2

        def flood(i,j, val):
            
            land[i][j] = val

            # down
            if 0<= i+1 < row and 0<= j < col:
                if land[i+1][j] ==1:
                    land[i+1][j] = val
                    flood(i+1,j, val)
                    
            # up
            if 0<= i-1 < row and 0<= j < col:
                if land[i-1][j] ==1:
                    land[i-1][j] = val
                    flood(i-1,j, val)
            # left
            if 0<= i < row and 0<= j-1 < col:
                if land[i][j-1] ==1:
                    land[i][j-1] = val
                    flood(i,j-1, val)
            # right
            if 0<= i < row and 0<= j+1 < col:
                if land[i][j+1] ==1:
                    land[i][j+1] = val
                    flood(i,j+1, val)
        

        for r in range(row):
            for c in range(col):
                if land[r][c] == 1:
                    flood(r,c, count)
                    count += 1

        # if no land groups
        if count == 2:
            return []

        co_ordinates,val = [],1

        # find co-ordinates of land
        for r in range(row):
            for c in range(col):
                if land[r][c]>val:
                    i,j,val = r,c, land[r][c]

                    # diagonal area
                    # if 0<= i+1 < row and 0 <= j+1 < col and land[i+1][j+1] == val:
                    #     while 0<= i+1 < row and 0 <= j+1 < col and land[i+1][j+1] == val:
                    #         i += 1
                    #         j += 1
                    #     # right area
                    #     while 0<= i < row and 0 <= j+1 < col and land[i][j+1] == val:
                    #         j += 1

                    # right area
                    if  0<= i < row and 0 <= j+1 < col and land[i][j+1] == val:

                        while 0<= i < row and 0 <= j+1 < col and land[i][j+1] == val:
                            j += 1

                    # down area
                    if  0<= i+1 < row and 0 <= j < col and land[i+1][j] == val:
                        while 0<= i+1 < row and 0 <= j < col and land[i+1][j] == val:
                            i += 1
                    
                    co_ordinates.append([r,c,i,j])
                    val = land[r][c]
        
        return co_ordinates
