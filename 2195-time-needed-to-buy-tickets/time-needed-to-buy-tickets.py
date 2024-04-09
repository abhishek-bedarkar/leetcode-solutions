class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ptr,l,result = 0, len(tickets),0
        
        while True:
            if tickets[ptr] ==0:
                ptr += 1
            else:
                tickets[ptr] -= 1
                result += 1
                ptr += 1

            if ptr == l:
                ptr = 0
            if tickets[k] == 0:
                return result 

            


        