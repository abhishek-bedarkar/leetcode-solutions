class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a_count = 0
        b_count = 0
        
        for i in range(0,len(colors)-2):
            if colors[i:i+3] == 'AAA':
                a_count += 1
            elif colors[i:i+3] == 'BBB':
                b_count += 1 

        if a_count == 0:
            return False
        elif a_count<=b_count:
            return False
        else:
            return True