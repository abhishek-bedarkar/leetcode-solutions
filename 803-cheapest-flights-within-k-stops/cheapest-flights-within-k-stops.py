class Solution:
    def __init__(self):
        self.matrix = None
    
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        # 1. DP approach
        matrix = [float('inf')] * n
        matrix[src] = 0

        for i in range(k + 1):
            temp = matrix[:]
            for flight in flights:
                if matrix[flight[0]] != float('inf'):
                    temp[flight[1]] = min(temp[flight[1]], matrix[flight[0]] + flight[2])
            matrix = temp
        
        return matrix[dst] if matrix[dst] != float('inf') else -1
        
        