import numpy as np
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check if number is not repeated in row
        for row in board:
            for r in row:
                if r != ".":
                    if row.count(r)>1:
                        return False

        # check if number is not repeated in col
        for i in range(len(board[0])):
            col = [row[i] for row in board]
            for c in col:
                if c!= ".":
                    if col.count(c)>1:
                        return False

        # check if number is not repeated in 3*3 block
        np_board = np.array(board)

        v_split = np.vsplit(np_board,3)
        final_block = [0]*9
        i=0
        for h in v_split:
            hs =  np.hsplit(h,3)
            for s in hs:
                final_block[i] = s
                i +=1

        for i,block in enumerate(final_block):
            final_block[i] = list(np.concatenate(final_block[i]))
       
        for block in final_block:
            for elm in block:
                if elm != "." and block.count(elm)>1:
                    return False
        return True
