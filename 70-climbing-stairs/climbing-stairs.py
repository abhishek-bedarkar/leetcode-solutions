class Solution:
    def climbStairs(self, n: int) -> int:
        mem = [0]*(n+1)
        return self.climbStair(0, n, mem)

    def climbStair(self, i:int, n:int, mem:List[int]) -> int:
        if i>n:
            return 0
        elif i==n:
            return 1
        
        if mem[i] > 0:
            return mem[i] 
        else:
            mem[i]=self.climbStair(i+1, n, mem) + self.climbStair(i+2, n, mem)

        return mem[i]