class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def check_word(b, w, i, j):
            if len(w) == 0:
                return True

            if 0<= i<rows and 0<= j< cols and b[i][j] == w[0] :
                #print('i ->',i ,'j ->',j,'found : ')  
                temp, b[i][j] = b[i][j], '-1'
                w = w.replace(w[0],"",1)
                #print('New word:', w)
                found =check_word(b, w,i,j-1) or check_word(b, w,i,j+1) or check_word(b, w,i-1,j) or check_word(b, w,i+1,j)
                b[i][j] = temp
                return found
            else:
                return False

        for i in range(rows):
            for j in range(cols):
                #print('check start for ',i,j, board[i][j])
                if check_word(board, word, i, j):
                    return True

        return False
            
        
        
        