class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Decimal to Binary approach
        # binary = bin(n)[2:]
        # print(binary)
        # if binary.count('1') == 1 and binary[0]=='1':
        #     return True
        # else:
        #     return False

        # Modulas approach
        if n <=0: return False
        if n==1: return True
        while n%2==0:
            n=n/2
        return n==1
        